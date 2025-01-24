import cloudinary
import cloudinary.uploader
import cloudinary.api
import os

INSTALLED_APPS += ['cloudinary', 'storages']

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'your-cloud-name',
    'API_KEY': 'your-api-key',
    'API_SECRET': 'your-api-secret'
}

AWS_ACCESS_KEY_ID = 'your-access-key'
AWS_SECRET_ACCESS_KEY = 'your-secret-key'
AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
AWS_S3_REGION_NAME = 'your-region'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
} 