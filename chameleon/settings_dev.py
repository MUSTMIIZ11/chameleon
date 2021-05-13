import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = "159.75.82.228"
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