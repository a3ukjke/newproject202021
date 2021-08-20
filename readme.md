python3 nameofproject/manage.py startapp blog
python3 nameofproject/manage.py startapp events

sozdat' model' 
models.py
from django.db import models
class Event(models.Model):
    event_image = models.ImageField(upload_to='')
    event_text = models.CharField(max_length=300)


python3 nameofproject/manage.py runserver 


You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

python3 nameofproject/manage.py migrate

Dobavim nawi prilozheniya apps blog and events

settings.py

INSTALLED_APPS = [
'events.apps.EventsConfig'
]
events - eto app
apps - nazvanie faila 
EventsConfig - /events/apps.py ----> class EventsConfig(AppConfig):

Sozdaem papku gde budut hranit'sya nawi fotki
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

apps neobhodimo razpolozhit' na odnom urovne manage.py



Sozdaem superuser

python3 nameofproject/manage.py createsuperuser
mangekyou
mangekyou


Register Event model
/events/admin.py
from.models import Event
admin.site.register(Event)

http://127.0.0.1:8000/admin/ появится Events - имя приложения

Создаем event
но ссылка на фото не работает
добааляем в nameofproject/urls.py

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/',views.first),
    path('second/',views.second, name='second'),
]    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



все фото сохраняются в /media/event_images


устанавливаем postgresql 

sudo -u postgres psql postgres

Подключаем postgresql к нашему проекту
изменить пароль для пользователя postgres
password postges
postgres
создаем базу данных 
CREATE DATABASE myawesomeblogdb;

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myawesomeblogdb',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

USE_TZ = False

Создаем приложение app blog
Создаем Модель в файле models.py
from django.db import models

class Post(models.Model):
    post_title = models.CharField(max_length=300)
    post_date = models.DateTimeField()
    post_text = models.TextField()
    post_image = models.ImageField(upload_to='event_images/')
В файле settings.py добавим в INSTALLED_APPS
INSTALLED_APPS = [
    'blog.apps.BlogConfig',]

BlogConfig берем с apps.py
python3 nameofproject/manage.py makemigrations
python3 nameofproject/manage.py migrate

Теперь регистрируем данное приложение через admin register
в файле admin.py
from django.contrib import admin

# Register your models here.
from .models import Post
admin.site.register(Post)


git add .
git commit -m "add post model"
git push -u origin main
a3ukjke



Создаем домашнюю страницу

в главной urls.py создаем путь     path('',events.views.home,name='home'),    <---- import events.views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
import events.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',events.views.home,name='home'),
    path('first/',views.first),
    path('second/',views.second, name='second'),
]    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


в events/views.py
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'events/home.html')


Создаем папки внутри приложения events такие как templates и внутри templates/events
создаем home.html внутри папки events/templates/events 

