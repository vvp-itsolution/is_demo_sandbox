from django.urls import path

from .views.move_one_day import (button_view, move_one_day, move_one_hour,
                                 move_one_week)

urlpatterns = [
    path('button_page/', button_view, name='button_page'),
    path('moveoneday/', move_one_day, name='move_one_day'),
    path('moveonehour/', move_one_hour, name='move_one_hour'),
    path('moveoneweek/', move_one_week, name='move_one_week'),
]
