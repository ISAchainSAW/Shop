from django.db import models
from django.urls import reverse


# Create your models here.
class Item(models.Model):
    itemsName = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    itemsCount = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    image = models.ImageField()

    def __str__(self):
        return self.itemsName

    def get_absolute_url(self):
        return reverse('item', args=[self.id])
