import settings
from django.contrib import admin
from django.urls import path, include
from post_currency.views import *
from django.conf.urls.static import static
from django.conf import settings
from start.views.start import start

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', start, name='start'),
    path('tasks/', include('tasks.urls')),
    path('ones/', include('ones_fresh_unf_with_b24.urls')),
    path('crmfields/', include('crmfields.urls')), # Поля сущностей
    path('moveonedayserver/', include('move_one_day_server.urls')), # Для переброса задачи на 1 час
    path('selectuser/', include('selectuser.urls')), # Для выбора пользователя
    path('company_on_maps/', include('company_on_maps.urls')), # Компании на карте


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
