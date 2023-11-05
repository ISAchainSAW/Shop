from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', index, name='home'),
    path('items/', cache_page(60)(pageItems.as_view()), name='items'),
    path('item/<slug:item_slug>/', pageItem.as_view(), name='item'),
    path('category/<slug:cat_slug>/', itemCategory.as_view(), name='category'),
    path('addItem/', addItem.as_view(), name='addItem'),
    path('login/', loginUser.as_view(), name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerUser.as_view(), name='register'),
    path('search/', search, name='search'),
]
