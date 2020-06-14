"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4*&*H)@#*(#@&U)*(u8hS)FU*SDHNFUDSHFDS(re#c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'notasquare.urad_web.apps.NotasquareUradWebConfig',
    'notasquare.urad_web_material.apps.NotasquareUradWebMaterialConfig',
    'application.apps.ApplicationConfig',
    #'django.contrib.admin',
    #'django.contrib.auth',
    #'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE_CLASSES = [
    #'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'application.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'application/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                #'django.contrib.auth.context_processors.auth',
                #'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'application.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':    'django.db.backends.mysql',
        'NAME':      'admin_db',
        'USER':      'root',
        'PASSWORD':  '123456',
        'HOST':      os.environ.get('DB_PORT_3306_TCP_ADDR'),
        'PORT':      os.environ.get('DB_PORT_3306_TCP_PORT')
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.autleaveh.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Logger
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level':      'DEBUG',
            'class':      'logging.FileHandler',
            'filename':   '/opt/debug.log'
        }
    },
    'loggers': {
        'default': {
            'handlers':   ['file'],
            'level':      'DEBUG',
            'propagate':  True
        }
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files
STATIC_URL = '/static/'
STATIC_ROOT = '/opt/web/static'

NOTASQUARE_API_URL = 'http://172.17.0.1:8610'

# Not A Square URAD
NOTASQUARE_URAD_CONTAINER = 'application.modules.common.containers.Container'
NOTASQUARE_URAD_TEST_CONTAINER = 'application.modules.common.containers.Container'
NOTASQUARE_RBAC_AUTHORIZATOR_SECURITY_CLASS = 'application.security'
NOTASQUARE_CONSUMERS_CONFIG_CLASS = 'application.consumers'
NOTASQUARE_MAX_ACTIVE_CONSUMERS = 10
