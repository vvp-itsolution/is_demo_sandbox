from django.urls import path

from .views.company_on_maps import maps


urlpatterns = [
    path('maps/', maps, name='maps'),
]