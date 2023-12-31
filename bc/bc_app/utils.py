# Файл для Mixins
from .models import *

menu = [{'link_name': 'Home', 'url_name': 'home'},
        {'link_name': 'Catalog', 'url_name': 'items'},
        {'link_name': 'Cart', 'url_name': 'cart_detail'},
        ]


class DataMixin():
    paginate_by = 3
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['cat'] = Category.objects.all()
        context['img'] = '/media/static/bc_app/images/logo.png'
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
