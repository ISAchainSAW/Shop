from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    # path('items/', pageItems, name='items'),
    path('items/', pageItems.as_view(), name='items'),
    path('item/<slug:item_slug>/', pageItem.as_view(), name='item'),
    # path('category/<slug:cat_slug>/', showCategory, name='category'),
    path('category/<slug:cat_slug>/', itemCategory.as_view(), name='category'),
    path('addItem/', addItem.as_view(), name='addItem'),
]
