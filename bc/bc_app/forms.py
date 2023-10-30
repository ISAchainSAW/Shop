from django import forms
from django.core.exceptions import ValidationError

from .models import *


# Форма не связана с конкретной моделью
# class AddItemForm(forms.Form):
#     itemsName = forms.CharField(max_length=50, label='Название предмета')
#     slug = forms.SlugField(max_length=255)
#     description = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':10}))
#     itemsCount = forms.IntegerField()
#     price = forms.IntegerField()
#     image = forms.ImageField()
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не выбрана')

# Форма связана с моделью
class AddItemForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'
    class Meta:
        model = Item  # Связь с моделью
        # fields = '__all__'  # Какие поля нужно отображать
        fields = ['itemsName', 'slug','description','itemsCount','image','price','cat'] # best practice
        widgets ={ #Словарь для изменения стиля полей
            'description': forms.Textarea(attrs={'cols':60, 'rows':10})
        }

    def clean_itemsName(self): #Пользовательский валидатор  начинается с clean_имяПоля
        itemsName = self.cleaned_data['itemsName'] # Получаем данные
        if len(itemsName) < 10:
            raise ValidationError('Длина меньше 10 символов')
        return itemsName
