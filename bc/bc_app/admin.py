from django.contrib import admin
from .models import Item


# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['itemsName','itemsCount','price']
    fields = ['itemsName','description',('itemsCount','price', 'image')]
    list_filter = ('itemsCount','price',)
    list_editable = ['price']


# admin.site.register(Item,ItemAdmin)
