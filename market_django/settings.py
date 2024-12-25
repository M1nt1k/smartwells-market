import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG')

ALLOWED_HOSTS = ['*', 'smartwells.ru', '*.smartwells.ru', '85.15.189.199', 'localhost', '127.0.0.1', '141.8.192.26']
CSRF_TRUSTED_ORIGINS = ['http://smartwells.ru']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'landing.apps.LandingConfig',
    'academy.apps.AcademyConfig',
    'news.apps.NewsConfig',
    'cart.apps.CartConfig',
    'checkout.apps.CheckoutConfig',
    'users.apps.UsersConfig',
    'taggit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'market_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'market_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': config('DB_NAME'),
		'HOST': config('DB_HOST'),
		'PORT': config('DB_PORT'),
		'USER': config('DB_USER'),
		'PASSWORD': config('DB_PASSWORD')
	}
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join (BASE_DIR, "static")

# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AUTH_USER_MODEL = 'users.ServiceUser'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')

EMAIL_HOST = config('EMAIL_HOST')                   # Сервер для отправки сообщений
EMAIL_HOST_USER = config('EMAIL_HOST_USER')         # имя пользователя
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD') # пароль от ящика
EMAIL_PORT = config('EMAIL_PORT')                   # порт для подключения
EMAIL_USE_TLS = config('EMAIL_USE_TLS')             # использование протокола шифрования
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')   # email, с которого будет отправлено письмо

TAGGIT_CASE_INSENSITIVE = True

if DEBUG:
    LOGIN_URL = 'users:login'
else:
    LOGIN_URL = 'users:keycloak_login'
LOGIN_REDIRECT_URL = 'academy:home'

KEYCLOAK_SERVER_URL = config('KEYCLOAK_SERVER_URL')
KEYCLOAK_REALM = config('KEYCLOAK_REALM')
KEYCLOAK_CLIENT_ID = config('KEYCLOAK_CLIENT_ID')
KEYCLOAK_CLIENT_SECRET = config('KEYCLOAK_CLIENT_SECRET')
KEYCLOAK_REDIRECT_URI = config('KEYCLOAK_REDIRECT_URI')