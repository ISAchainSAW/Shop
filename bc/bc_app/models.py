from django.db import models
from django.urls import reverse


# Create your models here.
class Item(models.Model):
    itemsName = models.CharField(max_length=50, verbose_name='Имя предмета')
    description = models.CharField(max_length=100, verbose_name='Описание предмета')
    itemsCount = models.IntegerField(default=0, verbose_name='Кол-во предметов')
    price = models.IntegerField(default=0, verbose_name='Цена')
    image = models.ImageField(upload_to='static/bc_app/images/',verbose_name='Изображение')
    cat = models.ForeignKey('Category', on_delete=models.CASCADE,
                            null=True, verbose_name='Категория')  # Django автоматически добавляет _id к названию FK, т.е на выходе cat_id

    class Meta:
        verbose_name = "Предмет" # Единственное число для класса
        verbose_name_plural = 'Предметы' #Множественное число для класса
        ordering = ['itemsName'] # Сортировка данных

    def __str__(self):
        return self.itemsName

    def get_absolute_url(self):
        return reverse('item', args=[self.pk])


class Category(models.Model):
    categoryName = models.CharField(max_length=50,
                                    db_index=True, verbose_name='Категория')  # db_index - означает, что это поле будет индексировано, те поиск по нему будет идти быстрее

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.categoryName

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
