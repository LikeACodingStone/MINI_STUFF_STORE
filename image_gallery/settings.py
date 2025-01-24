import os
from pathlib import Path
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 基础设置
DEBUG = False
ALLOWED_HOSTS = ['LikeACodingStone.pythonanywhere.com']

# 路径设置
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # 改为本地数据库
    }
}

# Cloudinary 设置
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET')
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gallery',
    'cloudinary',
    'cloudinary_storage',
]

# 安全设置
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
SECURE_SSL_REDIRECT = False

# 登录配置
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'gallery_view'

# 生产环境设置
DEBUG = False
ALLOWED_HOSTS = ['your_domain.com', 'localhost']

# 关闭 HTTPS 设置（因为 PythonAnywhere 已经提供）
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# 静态文件设置
STATIC_ROOT = '/home/your_username/your_project/static'

# Firebase 配置
FIREBASE_CONFIG = {
    "type": "service_account",
    "project_id": os.environ.get('FIREBASE_PROJECT_ID'),
    "private_key": os.environ.get('FIREBASE_PRIVATE_KEY').replace('\\n', '\n'),
    "client_email": os.environ.get('FIREBASE_CLIENT_EMAIL'),
} 