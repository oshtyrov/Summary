# В каталоге приложения создать модель, которая должна хранить информацию о поступивших товарах: название,
# дату поступления, цену, единицу измерения, имя поставщика. Выполнить миграции.

from django.db import models


class GoodsItem(models.Model):
    title = models.CharField(max_length=32, unique=True)
    date_of_receipt = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    unit = models.CharField(max_length=16)
    supplier_name = models.CharField(max_length=32)
    quantity = models.PositiveIntegerField()
