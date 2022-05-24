from django.forms import ModelForm

from pizza.models import Product, Price


class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'image', 'ingredients', 'about', 'cat']


class AddPriceForm(ModelForm):
    class Meta:
        model = Price
        fields = ['product', 'description', 'price']
