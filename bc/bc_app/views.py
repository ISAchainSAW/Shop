from django.shortcuts import render, get_object_or_404
from .models import Item


# Create your views here.
def index(request):
    context = {'asd': 'Privet'}
    return render(request, 'bc_app/index.html', context=context)


def pageItems(request):
    item = Item.objects.all()
    context = {'item': item}
    return render(request, 'bc_app/items.html', context=context)


def pageItem(request, id):
    item = get_object_or_404(Item, id=id)
    context = {'item': item}
    return render(request, template_name='bc_app/item.html', context=context)
