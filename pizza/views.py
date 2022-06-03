from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views import generic
from cart.forms import *

from .forms import AddProductForm
from .models import *
from .utils import DataMixin


def none(request):
    return HttpResponse('Page not exist')


class HomeView(DataMixin, generic.TemplateView):
    template_name = 'pizza/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))


class ProductCellView(DataMixin, generic.ListView):
    model = Product
    paginate_by = 9

    template_name = 'pizza/product_cells.html'
    context_object_name = 'products'

    def get(self, request, *args, **kwargs):
        return redirect('/pizza')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Список товаров')
        return dict(list(context.items()) + list(c_def.items()))


class ProductCellCategoryView(DataMixin, generic.ListView):
    model = Product
    paginate_by = 6

    template_name = 'pizza/product_cells.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(cat__slug=self.kwargs.get('cat_slug'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Список товаров')
        return dict(list(context.items()) + list(c_def.items()))


class ProductView(DataMixin, generic.FormView, generic.DetailView):
    model = Product
    form_class = CartAddProductForm

    template_name = 'pizza/product.html'
    pk_url_kwarg = 'product_id'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Просмотр товара')
        return dict(list(context.items()) + list(c_def.items()))


def user_logout(request):
    logout(request)
    return redirect('home')


class Test(DataMixin, generic.FormView):
    model = Product
    form_class = CartAddProductForm

    template_name = 'pizza/form.html'
    pk_url_kwarg = 'product_id'
    context_object_name = 'product'
