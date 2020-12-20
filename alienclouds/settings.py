from pathlib import Path
import django_heroku
import environ
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


DEBUG = True

ALLOWED_HOSTS = [
    'localhost',  # local
    '127.0.0.1',  # local
    '0.0.0.0',  # base-dir$ heroku local
    'alienclouds.herokuapp.com',  # heroku host
    'www.alienclouds.tk',  # dot.tk redirected domain
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'alienclouds_app',
    'cloudinary',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'alienclouds.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'alienclouds.wsgi.application'

env = environ.Env()
# reading .env file
environ.Env.read_env()

# # TUTORIAL: https://djangocentral.com/environment-variables-in-django/
# SECRET_KEY = env("SECRET_KEY")
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': env("DATABASE_NAME"),
#         'USER': env("DATABASE_USER"),
#         'PASSWORD': env("DATABASE_PASSWORD"),
#         'HOST': env("DATABASE_HOST"),
#         'PORT': env("DATABASE_PORT"),
#     }
# }

SECRET_KEY = 'j&o0esgkr_3-mjs9g*gf0#ud+4-$!5n1q%!b7)*ki6p^vx9q_i'
# HEROKU DATABASE
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'HOST': 'ec2-46-137-79-235.eu-west-1.compute.amazonaws.com',
         'NAME': 'd6i4ak9a8aql2b',
         'USER': 'bqytntsscuqftm',
         'PORT': '5432',
         'PASSWORD': '423c7ea3d6e174734d102065fd2e39c016c60069c55f34805a8697e221ccf7fb',
     }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())
