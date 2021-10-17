from django.forms import ModelForm
from mainapp.models import GoodsItem


class GoodsAddForm(ModelForm):
    class Meta:
        model = GoodsItem
        fields = ['title', 'price', 'unit', 'supplier_name', 'quantity']

    def __init__(self, *args, **kwargs):
        super(GoodsAddForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Введите название товара'
        self.fields['price'].widget.attrs['placeholder'] = 'Введите цену за еденицу товара'
        self.fields['unit'].widget.attrs['placeholder'] = 'Введите еденицу измерения товара'
        self.fields['supplier_name'].widget.attrs['placeholder'] = 'Введите поставщика товара'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Введите количество товара'

