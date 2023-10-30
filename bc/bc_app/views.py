from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from .utils import *


# Create your views here.
# Переделать в class
def index(request):
    context = {
        'asd': 'Privet',
        'img': '/media/static/bc_app/images/logo.png',
        'link_name': 'Catalog',
        'url_name': 'items'
    }
    return render(request, 'bc_app/index.html', context=context)


class pageItems(DataMixin, ListView):
    # Замена функции pageItems
    model = Item
    template_name = 'bc_app/items.html'
    context_object_name = 'item'

    # extra_context = {} # Переменная для передачи статических данных

    # Функция для получения статических+динамических данных
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # Получить уже существующий конеткст
        c_def = self.get_user_context()
        # Mixin в utils.py, для соблюдения DRY (Don't Repit Yourself)
        # Создает повторяющиеся элементы
        return dict(list(context.items()) + list(c_def.items()))

    # С помощью данной фукнции можно указывать что выбирать в виде списка из модели
    def get_queryset(self):
        return Item.objects.filter(itemsCount__gte=3)


# def pageItems(request):
#     item = Item.objects.all()
#     cat = Category.objects.all()
#     context = {
#         'item': item,
#         'cat': cat,
#         'cat_selected': 0,
#         'img': '/media/static/bc_app/images/logo.png',
#     }
#     return render(request, 'bc_app/items.html', context=context)


class pageItem(DataMixin, DetailView):
    model = Item
    template_name = 'bc_app/item.html'
    context_object_name = 'item'  # Если не определить переменную, тоже работает ???
    slug_url_kwarg = 'item_slug'  # Переопределение переменной в url, default = slug

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # Получить уже существующий конеткст
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


# def pageItem(request, item_slug):
#     item = get_object_or_404(Item, slug=item_slug)
#     context = {
#         'item': item,
#         'img': '/media/static/bc_app/images/logo.png',
#     }
#     return render(request, template_name='bc_app/item.html', context=context)


class itemCategory(DataMixin, ListView):
    model = Item
    template_name = 'bc_app/items.html'
    context_object_name = 'item'
    allow_empty = False  # если в списке нет ни 1 записи, то 404

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # Получить уже существующий конеткст
        c_def = self.get_user_context(cat_selected=context['item'][0].cat.slug)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Item.objects.filter(cat__slug=self.kwargs['cat_slug'])


# def showCategory(request, cat_slug):
#     cat = Category.objects.all()
#     cat_select = get_object_or_404(Category, slug=cat_slug)
#     item = Item.objects.filter(cat_id=cat_select.pk)
#     context = {
#         'item': item,
#         'cat': cat,
#         'cat_selected': cat_slug,
#         'img': '/media/static/bc_app/images/logo.png',
#     }
#     return render(request, 'bc_app/items.html', context=context)

class addItem(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddItemForm
    template_name = 'bc_app/addItem.html'
    success_url = reverse_lazy('items')
    login_url = reverse_lazy('items') # перенаправление неавторизованного пользователя

    # success_url = reverse_lazy('items') #куда перейти, после добавления формы
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # Получить уже существующий конеткст
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

# def addItem(request):
#     if request.method == 'POST':
#         form = AddItemForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#     else:
#         form = AddItemForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'bc_app/addItem.html', context=context)
