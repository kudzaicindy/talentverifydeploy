import os
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = os.environ.get('WEBSITE_HOSTNAME', 'localhost').split(',')
CSRF_TRUSTED_ORIGINS = ['https://' + host for host in ALLOWED_HOSTS]

DEBUG = False
SECRET_KEY = os.environ.get('MY_SECRET_KEY', 'a-default-secret-key')

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

CONNECTION = os.environ.get('AZURE_POSTGRESQL_CONNECTIONSTRING', '')
print(f"DEBUG: CONNECTION = {CONNECTION}")

if CONNECTION:
    # Parse the connection string
    conn_parts = dict(x.split('=') for x in CONNECTION.split(' ') if '=' in x)
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': conn_parts.get('dbname', 'talentverifydb'),
            'HOST': conn_parts.get('host', 'talent-verify-backend-server.postgres.database.azure.com'),
            'USER': conn_parts.get('user', 'rgntmemzbi@talent-verify-backend-server'),
            'PASSWORD': conn_parts.get('password', 'kudzai30'),
            'PORT': conn_parts.get('port', '5432'),
            'OPTIONS': {
                'sslmode': 'require',
            },
        }
    }
else:
    # Fallback to default SQLite database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

print(f"DEBUG: DATABASES = {DATABASES}")

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'