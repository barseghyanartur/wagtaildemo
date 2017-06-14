from .dev import *

# Django settings for django-fobi integration project.

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
)

TEMPLATES[0]['OPTIONS']['context_processors'] += [
    "fobi.context_processors.theme",  # Important!
    "fobi.context_processors.dynamic_values",  # Optional
    # "context_processors.testing",  # Testing
]
