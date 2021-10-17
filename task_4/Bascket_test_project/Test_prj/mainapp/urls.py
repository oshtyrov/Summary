from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('index/', mainapp.main, name='index'),
    path('form/', mainapp.add_product, name='form'),
]
