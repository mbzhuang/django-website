"""
Django settings for classproject project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '28!ivzrmvw+i@@iogodd3m%@7-nqg$o!n=@73+bt-zqay4e-c5'

DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0','127.0.0.1','serene-oasis-18729.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'website.apps.WebsiteConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'classproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'classproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Translate postgres
#        'NAME': 'kyfpqvjj',
#        'HOST': 'elmer-02.db.elephantsql.com',
#        'USER': 'kyfpqvjj',
#        'PASSWORD':'H18WFJXBDSbi-9mqBEJkW2gAUGmPoDRi',
#        'PORT':'5432'
#    }
#}

DATABASES = { 'default': {

  'ENGINE': 'django.db.backends.postgresql_psycopg2',
  'NAME': os.environ.get('DATABASE_NAME', ''),
  'HOST': os.environ.get('DATABASE_HOST', ''),
  'USER': os.environ.get('DATABASE_USER', ''),
  'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
  'PORT': os.environ.get('DATABASE_PORT', ''),

} }


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')



TWITTER_APP_KEY = os.environ.get('TWITTER_APP_KEY', '')
TWITTER_APP_SECRET = os.environ.get('TWITTER_APP_SECRET', '')
TWITTER_OAUTH_TOKEN = os.environ.get('TWITTER_OAUTH_TOKEN', '')
TWITTER_OAUTH_TOKEN_SECRET = os.environ.get('TWITTER_OAUTH_TOKEN_SECRET', '')

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'