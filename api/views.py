from rest_framework.generics import get_object_or_404

from api.permissions import IsAdminOrReadOnly, IsAdminOrCreateOnly
from api.serializers import *
from cart.models import Checkout
from pizza.models import *
from users.models import User
from rest_framework import viewsets, generics, authentication
from rest_framework import permissions
from django.shortcuts import render, HttpResponse


class CreateUserView(generics.CreateAPIView):
    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class UserUpdateDeliveryDataViewSet(generics.UpdateAPIView):
    serializer_class = UserUpdateDeliveryDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(email=self.request.user.email)

    def get_object(self):
        queryset = User.objects.filter(email=self.request.user.email)
        obj = get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]


class ProductCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

    # lookup_field = "cat__slug"
    # lookup_url_kwarg = "cat_slug"

    def get_queryset(self):
        return Product.objects.filter(cat__slug=self.kwargs.get('cat_slug'))


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    permission_classes = [IsAdminOrReadOnly]


class PriceCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = PriceSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return Price.objects.filter(product_id=self.kwargs.get('product_id'))


class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    permission_classes = [IsAdminOrCreateOnly]
