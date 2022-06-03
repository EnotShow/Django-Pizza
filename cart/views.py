from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.decorators.http import require_POST

from config import settings
from pizza.models import Price
from users.forms import UpdateUserDataForm
from users.models import User
from .cart import Cart
from .forms import CartAddProductForm
from .models import Checkout
from pizza.utils import context

@require_POST
@login_required
def cart_add(request, item_id):
    cart = Cart(request)
    product = get_object_or_404(Price, id=item_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart_detail')


@login_required
def cart_remove(request, item_id):
    cart = Cart(request)
    product = get_object_or_404(Price, id=item_id)
    cart.remove(product)
    return redirect('cart_detail')


@login_required
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    local_context = context
    local_context['cart'] = cart
    local_context['title'] = 'Корзина товаров'
    return render(request, 'cart/cart.html', context=local_context)


@login_required
def cart_data(request):
    session = request.session
    cart = session.get(settings.CART_SESSION_ID)
    return HttpResponse(f'{cart}')


@login_required
def checkout(request):
    order = Checkout
    cart = request.session.get(settings.CART_SESSION_ID)
    user_phone = request.user.phone
    user_address = request.user.address
    data_form = UpdateUserDataForm(
        request.POST,
        instance=request.user,
    )
    local_context = context
    local_context['form'] = data_form
    local_context['phone'] = user_phone
    local_context['address'] = user_address
    local_context['title'] = 'Оформление заказа'
    if request.session.get(settings.CART_SESSION_ID):

        if request.method == 'POST':
            if data_form.is_valid():
                data_form.save()
                order(user=request.user, order=cart).save()
                request.session[settings.CART_SESSION_ID] = {}
                return redirect('home')
            else:
                return render(request, 'cart/checkout.html', context=local_context)

        return render(request, 'cart/checkout.html', context=local_context)

    return render(request, 'cart/no_items_in_cart.html', context=local_context)
