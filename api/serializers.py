from rest_framework.fields import CurrentUserDefault

from cart.models import Checkout
from pizza.models import Product, Price
from users.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        return User.objects.create(
            email=validated_data['email'],
            password=validated_data['password'],
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'password']


class UserUpdateDeliveryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone', 'address']

    def update(self, instance, validated_data):
        instance.phone = validated_data['phone']
        instance.address = validated_data['address']
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class CheckoutSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=CurrentUserDefault())
    status = serializers.HiddenField(default=False)

    class Meta:
        model = Checkout
        fields = '__all__'
