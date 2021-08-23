# Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский,
# и дочерний классы получили новое значение цены. Следует проверить это, вызвав соответствующий метод
# родительского класса и функцию дочернего (функция, отвечающая за отображение информации о товаре в одной строке).


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def change_name(self, new_name):
        self.__name = new_name

    def change_price(self, new_price):
        self.__price = new_price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, __name, __prise):
        super().__init__(__name, __prise)

    def get_parent_data(self):
        return f'{self.get_name()} - {self.get_price()}.'


car = ItemDiscount('ford', 15000)
print(ItemDiscountReport.get_parent_data(car))
car.change_name('mazda')
car.change_price(16000)
print(ItemDiscountReport.get_parent_data(car))
