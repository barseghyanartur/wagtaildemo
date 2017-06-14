from .dev import *


def gettext(s):
    return s

# Django settings for django-fobi integration project.

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', gettext("English")),  # Main language!
    ('hy', gettext("Armenian")),
    ('nl', gettext("Dutch")),
    ('ru', gettext("Russian")),
    ('de', gettext("German")),
)

INSTALLED_APPS += (
    # Third party apps used in the project
    # 'tinymce',  # TinyMCE
    'easy_thumbnails',  # Thumbnailer
    'registration',  # Auth views and registration app

    # ***********************************************************************
    # ***********************************************************************
    # **************************** Fobi core ********************************
    # ***********************************************************************
    # ***********************************************************************
    'fobi',

    # ***********************************************************************
    # ***********************************************************************
    # ************************* Fobi form elements **************************
    # ***********************************************************************
    # ***********************************************************************

    # ***********************************************************************
    # **************************** Form fields ******************************
    # ***********************************************************************
    # 'fobi.contrib.plugins.form_elements.fields.birthday',
    'fobi.contrib.plugins.form_elements.fields.boolean',
    'fobi.contrib.plugins.form_elements.fields.checkbox_select_multiple',
    'fobi.contrib.plugins.form_elements.fields.date',
    'fobi.contrib.plugins.form_elements.fields.date_drop_down',
    'fobi.contrib.plugins.form_elements.fields.datetime',
    'fobi.contrib.plugins.form_elements.fields.decimal',
    'fobi.contrib.plugins.form_elements.fields.email',
    'fobi.contrib.plugins.form_elements.fields.file',
    'fobi.contrib.plugins.form_elements.fields.float',
    'fobi.contrib.plugins.form_elements.fields.hidden',
    'fobi.contrib.plugins.form_elements.fields.input',
    'fobi.contrib.plugins.form_elements.fields.integer',
    'fobi.contrib.plugins.form_elements.fields.ip_address',
    'fobi.contrib.plugins.form_elements.fields.null_boolean',
    'fobi.contrib.plugins.form_elements.fields.password',
    'fobi.contrib.plugins.form_elements.fields.radio',
    'fobi.contrib.plugins.form_elements.fields.range_select',
    'fobi.contrib.plugins.form_elements.fields.regex',
    'fobi.contrib.plugins.form_elements.fields.select',
    'fobi.contrib.plugins.form_elements.fields.select_model_object',
    'fobi.contrib.plugins.form_elements.fields.select_multiple',
    'fobi.contrib.plugins.form_elements.fields.select_multiple_with_max',
    'fobi.contrib.plugins.form_elements.fields.select_multiple_model_objects',
    'fobi.contrib.plugins.form_elements.fields.slider',
    'fobi.contrib.plugins.form_elements.fields.slug',
    'fobi.contrib.plugins.form_elements.fields.text',
    'fobi.contrib.plugins.form_elements.fields.textarea',
    'fobi.contrib.plugins.form_elements.fields.time',
    'fobi.contrib.plugins.form_elements.fields.url',

    # ***********************************************************************
    # ************************ Security elements ****************************
    # ***********************************************************************
    'fobi.contrib.plugins.form_elements.security.honeypot',

    # ***********************************************************************
    # ************************* Testing elements ****************************
    # ***********************************************************************
    'fobi.contrib.plugins.form_elements.test.dummy',

    # ***********************************************************************
    # ************************* Content elements ****************************
    # ***********************************************************************
    'fobi.contrib.plugins.form_elements.content.content_image',
    'fobi.contrib.plugins.form_elements.content.content_text',
    'fobi.contrib.plugins.form_elements.content.content_video',

    # ***********************************************************************
    # ***********************************************************************
    # ************************* Fobi form handlers **************************
    # ***********************************************************************
    # ***********************************************************************
    'fobi.contrib.plugins.form_handlers.db_store',
    'fobi.contrib.plugins.form_handlers.http_repost',
    'fobi.contrib.plugins.form_handlers.mail',

    # ***********************************************************************
    # ***********************************************************************
    # ************************* Fobi form importers *************************
    # ***********************************************************************
    # ***********************************************************************
    'fobi.contrib.plugins.form_importers.mailchimp_importer',

    # ***********************************************************************
    # ***********************************************************************
    # ************************** Fobi themes ********************************
    # ***********************************************************************
    # ***********************************************************************

    # ***********************************************************************
    # ************************ Bootstrap 3 theme ****************************
    # ***********************************************************************
    'fobi.contrib.themes.bootstrap3',  # Bootstrap 3 theme
    # DateTime widget
    'fobi.contrib.themes.bootstrap3.widgets.form_elements.'
    'datetime_bootstrap3_widget',

    'fobi.contrib.themes.bootstrap3.widgets.form_elements.'
    'date_bootstrap3_widget',

    # SliderPercentage widget
    'fobi.contrib.themes.bootstrap3.widgets.form_elements.'
    'slider_bootstrap3_widget',

    # ***********************************************************************
    # ************************ Foundation 5 theme ***************************
    # ***********************************************************************
    'fobi.contrib.themes.foundation5',  # Foundation 5 theme

    'fobi.contrib.themes.foundation5.widgets.form_handlers.'
    'db_store_foundation5_widget',

    # ***********************************************************************
    # **************************** Simple theme *****************************
    # ***********************************************************************
    'fobi.contrib.themes.simple',  # Simple theme

    # ***********************************************************************
    # ***********************************************************************
    # ************************ Fobi wagtail integration *********************
    # ***********************************************************************
    # ***********************************************************************
    'fobi.contrib.apps.wagtail_integration',
    'fobi_demo',
)

TEMPLATES[0]['OPTIONS']['context_processors'] += [
    "fobi.context_processors.theme",  # Important!
    "fobi.context_processors.dynamic_values",  # Optional
    # "context_processors.testing",  # Testing
]


# **************************************************************
# ************************ Fobi settings ***********************
# **************************************************************

# Fobi custom theme data for to be displayed in third party apps
# like `django-registraton`.
FOBI_CUSTOM_THEME_DATA = {
    'bootstrap3': {
        'page_header_html_class': '',
        'form_html_class': 'form-horizontal',
        'form_button_outer_wrapper_html_class': 'control-group',
        'form_button_wrapper_html_class': 'controls',
        'form_button_html_class': 'btn',
        'form_primary_button_html_class': 'btn-primary pull-right',
        'wagtail_integration': {
            'form_template_choices': [
                (
                    'fobi/bootstrap3_extras/view_embed_form_entry_ajax.html',
                    gettext("Custom bootstrap3 embed form view template")
                ),
            ],
            'success_page_template_choices': [
                (
                    'fobi/bootstrap3_extras/embed_form_entry_'
                    'submitted_ajax.html',
                    gettext("Custom bootstrap3 embed form entry submitted "
                            "template")
                ),
            ],
        },
    },
    'foundation5': {
        'page_header_html_class': '',
        'form_html_class': 'form-horizontal',
        'form_button_outer_wrapper_html_class': 'control-group',
        'form_button_wrapper_html_class': 'controls',
        'form_button_html_class': 'radius button',
        'form_primary_button_html_class': 'btn-primary',
        'wagtail_integration': {
            'form_template_choices': [
                (
                    'fobi/foundation5_extras/view_embed_form_entry_ajax.html',
                    gettext("Custom foundation5 embed form view template")
                ),
            ],
            'success_page_template_choices': [
                (
                    'fobi/foundation5_extras/embed_form_entry_submitted_'
                    'ajax.html',
                    gettext("Custom foundation5 embed form entry submitted "
                            "template")
                ),
            ],
        },
    },
    'simple': {
        'page_header_html_class': '',
        'form_html_class': 'form-horizontal',
        'form_button_outer_wrapper_html_class': 'control-group',
        'form_button_wrapper_html_class': 'submit-row',
        'form_button_html_class': 'btn',
        'form_primary_button_html_class': 'btn-primary',
        'wagtail_integration': {
        },
    }
}
