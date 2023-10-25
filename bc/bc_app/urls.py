from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('items/', pageItems, name='items'),
    path('item/<int:id>', pageItem, name='item'),
]