from django.shortcuts import render
from django.views import generic
from .models import Cart
from django.contrib.auth.decorators import login_required


class CartTemplateView(generic.TemplateView):
    template_name = 'cart/cart.html'


class CartListView(generic.ListView):
    model = Cart()
    template_name = 'cart/cart.html'

    context_object_name = 'cart'


class CartUpdateView(generic.UpdateView):
    model = Cart
    template_name = 'empty'


class CartDeleteView(generic.DeleteView):
    model = Cart
    template_name = 'empty'


class CheckoutView(generic.DetailView):
    template_name = 'empty'
