# Инкапсулировать оба параметра (название и цену) товара родительского класса.
# Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
# Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
# Результат выполнения заданий 1 и 2 должен быть идентичным.


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, __name, __price):
        super().__init__(__name, __price)

    def get_parent_data(self):
        return f'{self.get_name()} - {self.get_price()}.'


car = ItemDiscount('ford', 15000)
print(ItemDiscountReport.get_parent_data(car))


