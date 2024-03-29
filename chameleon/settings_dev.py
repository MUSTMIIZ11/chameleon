import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# URL = "159.75.82.228:9090"
URL = os.environ.get('DJANGO_HOST') or "127.0.0.1:8080"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'chameleon_db_dev',
        'USER': 'root',
        'PASSWORD': 'chameleon',
        'HOST': '159.75.82.228',
        'PORT': '3306',
    }
}