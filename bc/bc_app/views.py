from django.shortcuts import render, get_object_or_404
from .models import Item, Category


# Create your views here.
def index(request):
    context = {
        'asd': 'Privet',
        'img': '/media/static/bc_app/images/logo.png',
               }
    return render(request, 'bc_app/index.html', context=context)


def pageItems(request):
    item = Item.objects.all()
    cat = Category.objects.all()
    context = {
        'item': item,
        'cat': cat,
        'cat_selected': 0,
        'img': '/media/static/bc_app/images/logo.png',
    }
    print(context)
    return render(request, 'bc_app/items.html', context=context)


def pageItem(request, id):
    item = get_object_or_404(Item, id=id)
    context = {
        'item': item,
        'img': '/media/static/bc_app/images/logo.png',
               }
    return render(request, template_name='bc_app/item.html', context=context)


def showCategory(request, cat_id):
    item = Item.objects.filter(cat_id=cat_id)
    cat = Category.objects.all()
    context = {
        'item': item,
        'cat': cat,
        'cat_selected': cat_id,
        'img': '/media/static/bc_app/images/logo.png',
    }
    return render(request, 'bc_app/items.html', context=context)
