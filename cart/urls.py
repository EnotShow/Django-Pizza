from django.urls import path, include

from .views import *

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('cart/', cart_detail, name='cart_detail'),
    path('data/', cart_data),
    path('cart/add/<int:item_id>', cart_add, name='cart_add'),
    path('cart/remove/<int:item_id>/', cart_remove, name='cart_remove'),
]
