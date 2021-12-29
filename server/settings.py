"""
Django 3.1.3. settings for server project.
https://docs.djangoproject.com/en/3.1/topics/settings/
https://docs.djangoproject.com/en/3.1/ref/settings/

Google Analystics
id : G-30PG45RNS7  
"""

from pathlib import Path
import socket
import json
import os
SERVER_DEV_NAME = []
SERVER_GET_NAME = ""  # socket.gethostname()
BASE_DIR = Path(__file__).resolve().parent.parent
SERVER_TESTING_LOCAL_PSQL = True
SERVER_TESTING_LOCAL_SQLITE = False


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'main.apps.MainConfig',
    'service2020.apps.Service2020Config',
    'service2019.apps.Service2019Config',
]

# Whitelisting React Port Setting.
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'https://localhost:3000',
)

# REST_FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5
}

# SECURITY WARNING: don't run with debug turned on in production!
# https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
if SERVER_GET_NAME in SERVER_DEV_NAME:
    with open(os.path.join(BASE_DIR, "_key.json")) as f:
        SECRET_KEY = json.loads(f.read())["django"]
    ALLOWED_HOSTS = ["*"]
    DEBUG = True

# Web Service mode
else:
    with open("/etc/_key.json", "r") as f:
        SECRET_KEY = json.loads(f.read())["django"]
    ALLOWED_HOSTS = [
        "0.0.0.0",
        "127.0.0.1",
    ]
    DEBUG = False


# Web Service mode
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',     # NEW
    # 'django.middleware.cache.FetchFromCacheMiddleware',  # NEW
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]


ROOT_URLCONF = 'server.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.joinpath('templates')],
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
WSGI_APPLICATION = 'server.wsgi.application'


# Django Cache Framework
# https://docs.djangoproject.com/en/3.1/topics/cache/
CACHES = {
    "default": {
        # >> Local-memory caching
        # https://docs.djangoproject.com/en/3.1/topics/cache/#local-memory-caching
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-store",
    }
}

CACHE_MIDDLEWARE_ALIAS = 'default'  # which cache alias to use
# number of seconds to cache a page for (TTL)
CACHE_MIDDLEWARE_SECONDS = '600'
# should be used if the cache is shared across multiple sites that use the same Django instance
CACHE_MIDDLEWARE_KEY_PREFIX = ''


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# Application definition
SITE_ID = 1

# Development Mode
# DATABASE_CONFIG = {
#     "ENGINE": "django.db.backends.mysql",
#     "OPTIONS": {"read_default_file": BASE_DIR.joinpath("mysql.cnf"), },
# }


# local 에서 PSQL Server Test 조건
if SERVER_TESTING_LOCAL_PSQL:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }

# local 에서 SQLITE3 Server Test 조건
elif SERVER_TESTING_LOCAL_SQLITE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            # 'NAME': BASE_DIR.joinpath("db.sqlite3"),
            # 'NAME': str(BASE_DIR / 'db.sqlite3'),
        }
    }

# local 조건이 활성화 아닌경우
elif SERVER_GET_NAME in SERVER_DEV_NAME:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            # 'NAME': BASE_DIR.joinpath("db.sqlite3"),
            # 'NAME': str(BASE_DIR / 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = "Asia/Seoul"
USE_I18N = True
USE_L10N = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    (BASE_DIR.joinpath("static/dist")),
    # (BASE_DIR.joinpath("static")),
    # (BASE_DIR.joinpath("static/dist/y2020")),
    # ("media", BASE_DIR.joinpath("media")),
]
STATIC_ROOT = BASE_DIR.joinpath("staticfiles")

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath("media")
