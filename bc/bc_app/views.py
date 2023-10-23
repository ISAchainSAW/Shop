from django.shortcuts import render, get_object_or_404
from .models import Item


# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context=context)


def pageItems(request):
    item = Item.objects.all()
    return render(request, 'items.html', context={'item': item})


def pageItem(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, template_name='item.html', context={'item': item})
