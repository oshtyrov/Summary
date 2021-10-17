# Функции-контроллеры должны отвечать за загрузку списка товаров на главной странице и добавление товара на второй
# странице. ## 8. В файле views.py каталога проекта реализовать два контроллера в формате функций. Первый должен
# извлекать все записи из модели с каталогом товаром и передавать переменную со списком товаров в контекст шаблона
# (html-страница со списком товаров). Во втором контроллере должен создаваться объект формы для ввода данных о товаре
# и выполняться рендеринг шаблона страницы добавления товара. В контекст шаблона необходимо передавать объект формы.


from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from mainapp.models import GoodsItem
from mainapp.forms import GoodsAddForm
from django.shortcuts import render, HttpResponseRedirect


def main(request):
    context = {
        'title': 'GeekShop',
        'products': GoodsItem.objects.all(),
    }
    return render(request, 'mainapp/index.html', context)


def add_product(request):
    if request.method == 'POST':
        form = GoodsAddForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно добавили товар!')
            return HttpResponseRedirect(reverse('products:form'))
    else:
        form = GoodsAddForm()
    context = {'form': form}
    return render(request, 'mainapp/form.html', context)
