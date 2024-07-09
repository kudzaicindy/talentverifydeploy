import os 
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = os.environ.get('WEBSITE_HOSTNAME', 'localhost').split(',')
CSRF_TRUSTED_ORIGINS = ['https://' + host for host in ALLOWED_HOSTS]

DEBUG = False
SECRET_KEY = os.environ.get('MY_SECRET_KEY', 'a-default-secret-key')
DEBUG=False
SECRET_KEY=os.environ['MY_SECRET_KEY']

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
#CORS_ALLOWED_ORIGINS=[

#]

STORAGES={
    "default":{
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles":{
        "BACKEND":"whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
CONNECTION =os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
CONNECTION_STR={pair.split('=')[0]:pair.split('=')[1] for pair in CONNECTION.split(' ')}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': CONNECTION_STR['dbname'],
        'USER': CONNECTION_STR['user'],
        'PASSWORD':CONNECTION_STR['password'],
        'HOST': CONNECTION_STR['host'],
        
    }


}
STATIC_URL = '/static/'
STATIC_ROOT= BASE_DIR/'staticfiles'
