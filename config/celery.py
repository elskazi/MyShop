import os
from celery import Celery

# Задаем переменную окружения, содержащую название файла настроек нашего проекта.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('shop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# запускаем в командной сткроке, типа отправит тестовое барахло, в RabbinMQ можно удиветь скачки
# celery -A myshop worker -l info