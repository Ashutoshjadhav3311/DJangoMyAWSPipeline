"""
Django settings for notes project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import boto3
import json
import base64
from botocore.exceptions import ClientError
from pathlib import Path
#from notes.getcredentials.py import getdjangokey,getdbkey
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

 
def getdjangokey():
 
# AWS Secrets Manager to use AWS credentials & Django secret Key stored there
    secret_name = "sonarcloudDjangoSecreat"  
    region_name="us-west-2"
 
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
 
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        # Handle the exception based on the error code
        raise e
    else:
        # Decrypts secret using the associated KMS CMK
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            djangosecret_dict = json.loads(secret)
#            print("Retrieved secret:", secret_dict)  # Testing line
            return djangosecret_dict
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
            return json.loads(decoded_binary_secret)    
 
def getdbkey():
 
# AWS Secrets Manager to use AWS credentials & Django secret Key stored there
    secret_name = "databaseSecret"  
    region_name="us-west-2"
 
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
 
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        # Handle the exception based on the error code
        raise e
    else:
        # Decrypts secret using the associated KMS CMK
        if 'SecretString' in get_secret_value_response:
            dbsecret = get_secret_value_response['SecretString']
            dbsecret_dict = json.loads(dbsecret)
#            print("Retrieved secret:", secret_dict)  # Testing line
            return dbsecret_dict
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
            return json.loads(decoded_binary_secret)    
 
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
djangokey=getdjangokey()
SECRET_KEY = djangokey['key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['x22183868djangoo.eba-uzpbfmvh.eu-west-1.elasticbeanstalk.com',
                'djangospacenotes2-env.eba-pvcmvxb4.us-west-2.elasticbeanstalk.com']

LOGIN_REDIRECT_URL = '/'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notesapp'
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

ROOT_URLCONF = 'notes.urls'

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

WSGI_APPLICATION = 'notes.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
dbkey=getdbkey()
googleAPIkey=dbkey['googleapikey']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': dbkey['dbname'],  
        'USER': dbkey['username'],  
        'PASSWORD': dbkey['password'], 
        'HOST': dbkey['host'],  
        'PORT': dbkey['port'], 
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
GOOGLE_MAPS_API_KEY = googleAPIkey
STATICFILES_DIRS = [BASE_DIR/'static']
