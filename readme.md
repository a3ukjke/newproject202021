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



