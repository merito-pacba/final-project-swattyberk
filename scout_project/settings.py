import os
from pathlib import Path

# Projenin ana dizini
BASE_DIR = Path(__file__).resolve().parent.parent

# GÜVENLİK UYARISI: Bu anahtarı gerçek yayında gizli tut!
SECRET_KEY = 'django-insecure-kendi-anahtarin-burada-kalsin'

# GÜVENLİK UYARISI: Yayına alırken bunu False yap!
DEBUG = True

ALLOWED_HOSTS = ['proje-hhfadbfkgnccdnfg.polandcentral-01.azurewebsites.net', 'localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Kendi uygulamalarını buraya ekle
    'players', # Eğer uygulamanın adı players ise
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# BURASI ÇOK ÖNEMLİ: index.html'i bulması için
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Burayı bu şekilde güncelle
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

# Proje ismine göre burayı kontrol et (FUTBOL_PROJECT.wsgi gibi)
WSGI_APPLICATION = 'scout_project.wsgi.application'
ROOT_URLCONF = 'scout_project.urls'

# Veritabanı (Şimdilik SQLite en iyisi)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Şifre doğrulama vb. (Buralara dokunmana gerek yok)
LANGUAGE_CODE = 'tr-tr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# STATİK VE MEDYA DOSYALARI (Fotoğrafların görünmesi için şart)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'