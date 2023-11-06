from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from bc_app.models import Item
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        if item_id in cart.cart:
            if cd['quantity'] + cart.cart[item_id]['quantity'] > item.itemsCount:
                cd['quantity'] = 0
        else:
            if cd['quantity'] > item.itemsCount:
                cd['quantity'] = item.itemsCount
        cart.add(item=item,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.remove(item)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    context = {
        'cart': cart,
        'img': '/media/static/bc_app/images/logo.png'
    }
    return render(request, 'cart/detail.html', context=context)
