from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', none, name='about'),
    path('products/', ProductCellView.as_view(), name='products'),
    path('logout/', user_logout, name='logout'),
    path('<slug:cat_slug>/', ProductCellCategoryView.as_view(), name='cat'),
    path('products/<int:product_id>', ProductView.as_view(), name='product'),
]
