from django.urls import path

from .views import *

urlpatterns = [
    path('add_cart<int:item_id>', add_to_cart, name='add_to_cart'),
]
