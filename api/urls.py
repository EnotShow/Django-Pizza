from django.urls import path, include
from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'checkout', CheckoutViewSet)
router.register(r'products', ProductViewSet)
router.register(r'prices', PriceViewSet)

urlpatterns = [
    path('api-register', CreateUserView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('user/', UserUpdateDeliveryDataViewSet.as_view()),
    path('', include(router.urls)),
    path('product_cat/<slug:cat_slug>/', ProductCategoryViewSet.as_view({'get': 'list'})),
    path('products/<int:product_id>/prices', PriceCategoryViewSet.as_view({'get': 'list'})),
]
