 <h1>Первый раз пробую Django</h1>

<h2>Подготовока</h2>
<p>1. Создать дерикторию для работы</p>
<p>2. Создать venv в созданной директории и активиривать ее (Install: python3 -m venv venv. Activart: activate)</p>
<p>3. В активированой среде установить django (pip3 install django)</p>
<p>4. Создать новйы проект (django-admin.py startproject learning_log) <b>! в конце точку</b></p>


<h2>Работа над проектом</h2>
<p>1. Создание БД</p>
После создание проекта необходимо создать БД командой<br>
<b>python3 manage.py migrate</b><br>
Каждое изменение базы данных называется миграцией
<p>2. Запуск проекта</p>
Для запуска сервера разработки необходимо выполнить команду<br>
<b>python3 manage.py runserver</b>
<p>3. Работа на приложением</p>
Проект Django представляет собой группу отдельных приложений. Приложений может быть много который вливаются в один проект.
Что бы создать инфраструктуру под приложение необходимо написать команду<br>
<b>python3 manage.py startapp {название приложения}</b>
Особое внимание требуют файлы models.py, admin.py и views.py
<p>4. Определение models</p>
Модель сообщает Django как работать с данными которые будут храниться в приложении. Модель представляет собой обычный класс. Она содержитатрибуты и методы
Что бы использвоать модель после ее создания нужно подключить приложение в Settings -> INSTALLED_APPS<br>
Затем создать миграцию <b> python manage.py makemigrations</b> применить ее <b> python manage.py migrate</b>
<p>5. Админка</p>
Для активации админки необходимо создать суперпользователя командой<br>
<b> python manage.py createsuperuser</b>
<p>6. Регистрация моделей в админке</p>
Что бы модель отобразилась в админке ее нужно зарегистрировать в ней<br>
admin.py -> admin.site.register(имя модели)
<p>7. Интерактивная оболочка</p>
Можно использовать для работы с информацией в БД<br>
<b>Команда: python3 manage.py shell</b><br>
<b>Пример: from learning_logs.models import Topic</b><br>
<b>Получить все экземпляры  модели Topic: Topic.objects.all()</b> возвращаемый список называется
итоговым набором (queryset)