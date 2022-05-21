from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views import generic

from .models import *


def none(request):
    return HttpResponse('Page not exist')


class HomeView(generic.TemplateView):
    template_name = 'pizza/index.html'


class ProductCellView(generic.ListView):
    model = Product
    paginate_by = 9

    template_name = 'pizza/product_cells.html'
    context_object_name = 'products'

    def get(self, request, *args, **kwargs):
        return redirect('/pizza')


class ProductCellCategoryView(generic.ListView):
    model = Product
    paginate_by = 9

    template_name = 'pizza/product_cells.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(cat__slug=self.kwargs.get('cat_slug'))


class ProductView(generic.DetailView):
    model = Product

    template_name = 'pizza/product.html'
    pk_url_kwarg = 'product_id'
    context_object_name = 'product'


def user_logout(request):
    logout(request)
    return redirect('home')
