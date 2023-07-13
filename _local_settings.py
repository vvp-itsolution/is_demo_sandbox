# Пример local_settings
# Измените данные на свои

DEBUG = True
ALLOWED_HOSTS = ['*']

from integration_utils.bitrix24.local_settings_class import LocalSettingsClass

APP_SETTINGS = LocalSettingsClass(
    portal_domain='pavelkovvv.bitrix24.ru',
    app_domain='0.0.0.0:8000',
    app_name='is_demo',
    salt='wefiewofioiI(IF(Eufrew8fju8ewfjhwkefjlewfjlJFKjewubhybfwybgybHBGYBGF',
    secret_key='wefewfkji4834gudrj.kjh237tgofhfjekewf.kjewkfjeiwfjeiwjfijewf',
    application_bitrix_client_id='local.64a419fe427f68.28147804',
    application_bitrix_client_secret='4SQ11NGpVjVpS30arHU7Xc2i106zkK6BU5DJwhaH7DjmATAmki',
    application_index_path='/',
)



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'is_demo',  # Or path to database file if using sqlite3.
        'USER': 'is_demo',  # Not used with sqlite3.
        'PASSWORD': 'password',  # Not used with sqlite3.
        'HOST': 'localhost',
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
