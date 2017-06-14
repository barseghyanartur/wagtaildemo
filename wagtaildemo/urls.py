from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView

from fobi.settings import DEFAULT_THEME

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.contrib.wagtailapi import urls as wagtailapi_urls
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.api.v2.endpoints import PagesAPIEndpoint
from wagtail.wagtaildocs.api.v2.endpoints import DocumentsAPIEndpoint
from wagtail.wagtailimages.api.v2.endpoints import ImagesAPIEndpoint

from demo import views


api = WagtailAPIRouter('api')
api.register_endpoint('pages', PagesAPIEndpoint)
api.register_endpoint('images', ImagesAPIEndpoint)
api.register_endpoint('documents', DocumentsAPIEndpoint)

# Mapping.
fobi_theme_home_template_mapping = {
    'bootstrap3': 'home/bootstrap3.html',
    'foundation5': 'home/foundation5.html',
    'simple': 'home/simple.html',
}

# Get the template to be used.
fobi_home_template = fobi_theme_home_template_mapping.get(
    DEFAULT_THEME,
    'home/base.html'
)

FOBI_EDIT_URLS_PREFIX = ''
if DEFAULT_THEME in ('simple', 'djangocms_admin_style_theme'):
    FOBI_EDIT_URLS_PREFIX = 'admin/'

urlpatterns = []

url_patterns_args = [
    # DB Store plugin URLs
    url(r'^fobi/plugins/form-handlers/db-store/',
        include('fobi.contrib.plugins.form_handlers.db_store.urls')),
    url(r'^fobi/plugins/form-wizard-handlers/db-store/',
        include('fobi.contrib.plugins.form_handlers.db_store.urls.'
                'form_wizard_handlers')),

    # django-fobi URLs:
    url(r'^fobi/', include('fobi.urls.view')),
    url(r'^{0}fobi/'.format(FOBI_EDIT_URLS_PREFIX),
        include('fobi.urls.edit')),

    url(r'^django-admin-tools/', include('admin_tools.urls')),

    url(r'^django-admin/', include(admin.site.urls)),

    # django-registration URLs:
    url(r'^accounts/', include('registration.backends.simple.urls')),

    url(r'^$', TemplateView.as_view(template_name=fobi_home_template)),
]

urlpatterns += i18n_patterns(*url_patterns_args)

urlpatterns += [
    # url(r'^django-admin/', include(admin.site.urls)),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'search/$', views.search, name='search'),
    url(r'^api/', include(wagtailapi_urls)),
    url(r'^api/v2/', include(api.urls)),
]

# Conditionally including Django REST framework integration app
if 'fobi.contrib.apps.drf_integration' in settings.INSTALLED_APPS:
    from fobi.contrib.apps.drf_integration.urls import fobi_router
    urlpatterns += [
        url(r'^api/', include(fobi_router.urls))
    ]

# Conditionally including Captcha URls in case if
# Captcha in installed apps.
if getattr(settings, 'ENABLE_CAPTCHA', False):
    try:
        from captcha.fields import ReCaptchaField
    except ImportError:
        try:
            from captcha.fields import CaptchaField
            if 'captcha' in settings.INSTALLED_APPS:
                urlpatterns += [
                    url(r'^captcha/', include('captcha.urls')),
                ]
        except ImportError:
            pass

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.views.generic.base import RedirectView

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        url(
            r'^favicon\.ico$', RedirectView.as_view(
                url=settings.STATIC_URL + 'demo/images/favicon.ico'
            )
        )
    ]

    # Uncomment the lines below to enable django-debug-toolbar (along with the
    # corresponding lines in settings/local.py):
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
           url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns


# For anything not caught by a more specific rule above, hand over to
# Wagtail's serving mechanism (must come last)
urlpatterns += [
    url(r'', include(wagtail_urls)),
]
