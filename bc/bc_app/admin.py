from django.contrib import admin
from .models import Item, Category


# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['itemsName','itemsCount','price',]
    fields = ['slug','itemsName','description',('itemsCount','price', 'image'),'cat']
    prepopulated_fields = {'slug': ('itemsName',)}
    search_fields = ('itemsName',) # если один элемент создавать кортеж, или []
    list_filter = ('itemsCount','price',)
    list_editable = ['price']
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['categoryName']
    fields = ['categoryName','slug']
    prepopulated_fields = {'slug':('categoryName',)}
# admin.site.register(Item,ItemAdmin)
