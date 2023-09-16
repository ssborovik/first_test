import os
import django
import random
# Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")  # Замените на путь к вашим настройкам Django
django.setup()
# Теперь вы можете импортировать и использовать модели Django
from learning_logs.models import Topic, Entry

topics = [
    'Rock Climbing',
    'Chess'
]
my_list = [
    "Привет, мир!",
    "Это пример текста.",
    "Python - отличный язык программирования.",
    "Здесь можно добавить еще несколько текстовых элементов.",
    "Список может содержать разные данные.",
    "Для чего вам нужен этот список?"
]

top = Topic.objects.all()

for i in my_list:
    my_data = Entry(text=i, topic=random.choice(top))
    my_data.save()