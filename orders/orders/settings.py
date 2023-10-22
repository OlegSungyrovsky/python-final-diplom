"""
Django settings for orders project.

Generated by 'django-admin startproject' using Django 2.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

from dotenv import load_dotenv

load_dotenv()
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get('DEBUG', default=0))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')

# Application definition

INSTALLED_APPS = [
    'baton',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',
    'rest_framework',
    'rest_framework.authtoken',
    'django_rest_passwordreset',
    'django_celery_results',
    'versatileimagefield',
    'social_django',
    'drf_spectacular',
    'drf_yasg',
    'silk',

    'backend.apps.BackendConfig',
    'baton.autodiscover',
]

MIDDLEWARE = [
    'silk.middleware.SilkyMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'orders.urls'

INTERNAL_IPS = [
    '127.0.0.1',
]

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'orders.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('NAME', 'my_diplom'),
        'PORT': os.environ.get('PORT', '5432'),
        'HOST': os.environ.get('HOST', '127.0.0.1'),
        'USER': os.environ.get('USER', 'postgres'),
        'PASSWORD': os.environ.get('PASSWORD', '1234')
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

MEDIA_URL = '/media/'

TEST_IMAGE_PATH = os.path.join(BASE_DIR, 'tests/backend/test_image/')

AUTH_USER_MODEL = 'backend.User'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
# EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
SERVER_EMAIL = EMAIL_HOST_USER

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 40,

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),

    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),

    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '10000/day'
    },

    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

APPEND_SLASH = False

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', default='redis://redis:6379/0')
CELERY_BROKER_TRANSPORT = os.environ.get('CELERY_BROKER_TRANSPORT', default='redis')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', default='django-db')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orders.settings')

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.mailru.MRGOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

SOCIAL_AUTH_JSONFIELD_ENABLED = True
SOCIAL_AUTH_USER_MODEL = 'backend.User'
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']

SOCIAL_AUTH_GITHUB_KEY = os.environ.get('SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = os.environ.get('SOCIAL_AUTH_GITHUB_SECRET')
SOCIAL_AUTH_GITHUB_SCOPE = ['user']

SOCIAL_AUTH_MAILRU_KEY = os.environ.get('SOCIAL_AUTH_MAILRU_KEY')
SOCIAL_AUTH_MAILRU_SECRET = os.environ.get('SOCIAL_AUTH_MAILRU_SECRET')

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Token': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

BATON = {
    'SITE_HEADER': 'My diploma',
    'SITE_TITLE': 'My diploma',
    'INDEX_TITLE': 'Backend',
    'SUPPORT_HREF': 'https://github.com/OlegSungyrovsky',
    'COPYRIGHT': 'copyright © 2023 <a href="https://github.com/OlegSungyrovsky">Oleg srl</a>',
    'POWERED_BY': '<a href="https://github.com/OlegSungyrovsky">Oleg srl</a>',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'CHANGELIST_FILTERS_IN_MODAL': True,
    'CHANGELIST_FILTERS_ALWAYS_OPEN': False,
    'CHANGELIST_FILTERS_FORM': True,
    'COLLAPSABLE_USER_AREA': False,
    'MENU_ALWAYS_COLLAPSED': False,
    'MENU_TITLE': 'Menu',
    'MESSAGES_TOASTS': False,
    'GRAVATAR_ENABLED': False,
    'FORCE_THEME': None,
    'LOGIN_SPLASH': 'https://mykaleidoscope.ru/x/uploads/posts/'
                    '2022-09/1663154918_37-mykaleidoscope-ru-p-buenos-aires-argentina-krasivo-38.jpg',
    'MENU': (
        {'type': 'title', 'label': 'main', 'apps': ('auth', 'rest_framework.authtoken')},
        {
            'type': 'app',
            'name': 'auth',
            'label': 'Authentication',
            'models': (
                {
                    'name': 'group',
                    'label': 'Groups'
                },

            )
        },
        {
            'type': 'app',
            'name': 'authtoken',
            'label': 'Rest Authentication Token',
        },
        {
            'type': 'app',
            'name': 'social_django',
            'label': 'Social Django',
        },
        {
            'type': 'app',
            'name': 'django_celery_results',
            'label': 'Celery',
        },
        {
            'type': 'app',
            'name': 'django_rest_passwordreset',
            'label': 'Password Reset',
        },
        {
            'type': 'app',
            'name': 'backend',
            'label': 'Confirm Email',
            'models': (
                {
                    'name': 'confirmemailtoken',
                    'label': 'Confirm Email Token'
                },
            )
        },
        {
            'type': 'app',
            'name': 'backend',
            'label': 'User',
            'default_open': True,
            'models': (
                {
                    'name': 'user',
                    'label': 'Users'
                },
                {
                    'name': 'contact',
                    'label': 'Contacts'
                },
                {
                    'name': 'confirmemailtoken',
                    'label': 'Confirm Email Tokens'
                }
            )
        },
        {
            'type': 'app',
            'name': 'backend',
            'label': 'Shop',
            'default_open': True,
            'models': (
                {
                    'name': 'shop',
                    'label': 'Shop'
                },
                {
                    'name': 'shopimport',
                    'label': 'Shop Import'
                }
            )
        },
        {
            'type': 'app',
            'name': 'backend',
            'label': 'Products',
            'default_open': True,
            'models': (
                {
                    'name': 'category',
                    'label': 'Category'
                },
                {
                    'name': 'product',
                    'label': 'Product'
                },
                {
                    'name': 'productinfo',
                    'label': 'Product Info'
                },
                {
                    'name': 'parameter',
                    'label': 'Parameter'
                },
                {
                    'name': 'productparameter',
                    'label': 'Product Parameter'
                },
            )
        },
        {
            'type': 'app',
            'name': 'backend',
            'label': 'Orders',
            'default_open': True,
            'models': (
                {
                    'name': 'order',
                    'label': 'Order'
                },
                {
                    'name': 'orderitem',
                    'label': 'Order Item'
                }
            )
        },

        {'type': 'free',
         'label': 'Documentation Swagger Redoc',
         'url': 'http://localhost:8000/redoc/',
         },
        {'type': 'free',
         'label': 'Documentation Swagger ',
         'url': 'http://localhost:8000/swagger/',
         },
        {'type': 'free',
         'label': 'Documentation Postmen ',
         'url': 'https://documenter.getpostman.com/view/24872439/2s9YJez1xd',
         },
    ),
    'ANALYTICS': {
        'CREDENTIALS': os.path.join(BASE_DIR, 'credentials.json'),
        'VIEW_ID': os.environ.get('ANALYTICS_VIEW_ID', default='11111'),
    }
}

VERSATILEIMAGEFIELD_SETTINGS = {
    'cache_length': 2592000,
    'cache_name': 'versatileimagefield_cache',
    'jpeg_resize_quality': 70,
    'create_images_on_demand': True,
    'image_key_post_processor': None,
}

VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    'person_image': [
        ('full_size', 'url'),
        ('thumbnail', 'thumbnail__100x100'),
    ]
}
