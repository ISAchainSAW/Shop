from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Item, Category
from .forms import AddItemForm


# Create your views here.
def index(request):
    context = {
        'asd': 'Privet',
        'img': '/media/static/bc_app/images/logo.png',
    }
    return render(request, 'bc_app/index.html', context=context)


class pageItems(ListView):
    # Замена функции pageItems
    model = Item
    template_name = 'bc_app/items.html'
    context_object_name = 'item'

    # extra_context = {} # Переменная для передачи статических данных

    # Функция для получения статических+динамических данных
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # Получить уже существующий конеткст
        context['cat_selected'] = 0
        context['cat'] = Category.objects.all()
        context['img'] = '/media/static/bc_app/images/logo.png'
        return context

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


class pageItem(DetailView):
    model = Item
    template_name = 'bc_app/item.html'
    context_object_name = 'item'  # Если не определить переменную, тоже работает ???
    slug_url_kwarg = 'item_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # Получить уже существующий конеткст
        context['img'] = '/media/static/bc_app/images/logo.png'
        return context


# def pageItem(request, item_slug):
#     item = get_object_or_404(Item, slug=item_slug)
#     context = {
#         'item': item,
#         'img': '/media/static/bc_app/images/logo.png',
#     }
#     return render(request, template_name='bc_app/item.html', context=context)


class itemCategory(ListView):
    model = Item
    template_name = 'bc_app/items.html'
    context_object_name = 'item'
    allow_empty = False  # если в списке нет ни 1 записи, то 404

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # Получить уже существующий конеткст
        context['cat'] = Category.objects.all()
        context['cat_selected'] = context['item'][0].cat.slug
        context['img'] = '/media/static/bc_app/images/logo.png'
        return context

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

class addItem(CreateView):
    form_class = AddItemForm
    template_name = 'bc_app/addItem.html'
    # success_url = reverse_lazy('items') #куда перейти, после добавления формы
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # Получить уже существующий конеткст
        context['img'] = '/media/static/bc_app/images/logo.png'
        return context

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
