"""


python manage.py startapp coupons

pip install celery  Задачник
pip install flower  Вебморда задачника
pip install stripe   Платилка
pip install weasyprint  #PDFgenerator
# For windowsd - Install MSYS2 ,Install GTK3 DLL, прописать Path, перезагрузить пк


docker pull rabbitmq
# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
# celery -A shop worker -l info



"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4&(!=sgb+o)=+m#_1%4f#5q+++f@@&jyn2pk(6!w%cffwy$%u+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop.apps.ShopConfig',  # Магазин
    'cart.apps.CartConfig',  # Корзина
    'orders.apps.OrdersConfig',  # Заказы
    'payment.apps.PaymentConfig',  # платежная система
    'coupons.apps.CouponsConfig', # купоны
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Это промежуточный слой для управления сессиями.
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # контекстный процессор
                'cart.context_processors.cart',
            ],
            # темплейттэг для  склонения численности товаров ru_plural
            'builtins': ['shop.templatetags.prod_extras'],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Хранение данных корзины в сессии
CART_SESSION_ID = 'cart'

# В случае если вы хотите использовать отправку почты в тестовом режиме (в консоли), раскомментируйте первую строку.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # для консоли

# YANDEX Шестерня- Все настройки - Почтовые программы - Разрешить доступ к почтовому ящику с помощью почтовых клиентов
# С сервера imap.yandex.ru по протоколу IMAP
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # для реальной отправки
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'elskazi@yandex.ru'
EMAIL_HOST_PASSWORD = ' '

# Платилка

STRIPE_PUBLISHABLE_KEY = 'pk_test_51N8LiYERlNEa02L1zb315Im54ZIQEqA6mhSeX6TABQFQ0zTuuhUgkq54MyHDGbxXuYEIDS9usI3YXlZOABcfoIaN003Cxvxesb'  # Publishable key
STRIPE_SECRET_KEY = 'sk_test_51N8LiYERlNEa02L1I2ZPqGHGdIsP620dbsm5C120uPtNI5she5O1KSPEW35ltmcKdxJJMTsjDsp6gTFXACrfX32900y7JwLHex'  # Secret key
STRIPE_API_VERSION = '2022-11-15'
STRIPE_WEBHOOK_SECRET = 'whsec_3508b777688cb6d06fb7a0d0561af493174f8ec9e0b962f6022fd08025ab8517'
