from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from bc_app.models import Item


def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         item=item['item'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # Изменение кол-ва на складе
            for pk, item in cart.cart.items():
                c = Item.objects.get(pk=pk)
                c.itemsCount -= item['quantity']
                c.save()

            # очистка корзины
            cart.clear()
            return render(request, 'orders/created.html',
                          {'order': order, 'img': '/media/static/bc_app/images/logo.png'})
    else:
        form = OrderCreateForm
    return render(request, 'orders/create.html',
                  {'cart': cart, 'form': form, 'img': '/media/static/bc_app/images/logo.png'})
