
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-t=35cl4(i-wwhb_235e3(cy8rtjs!8)d@if^%qb-v3zdld9a5y'

DEBUG = True

ALLOWED_HOSTS = []


# INSTALLED_APPS = [
#     'django_tenants',
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'customers.apps.CustomersConfig',
#     'core'
# ]

SHARED_APPS = (
    'django_tenants',
    'customers',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
)

TENANT_APPS = (
    'core',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
)
INSTALLED_APPS = list(set(SHARED_APPS + TENANT_APPS))


MIDDLEWARE = [
'django_tenants.middleware.TenantMainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'schoolsaas.urls'


DATABASE_ROUTERS = ('django_tenants.routers.TenantSyncRouter',)

TENANT_MODEL = "customers.Client"
TENANT_DOMAIN_MODEL = "customers.Domain"


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'schoolsaas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME':'postgres',
        'USER':'postgres',
        'PASSWORD':'mysecretpassword',
        'HOST':'localhost',
        'PORT':'5432',
    }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'