# Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в
# дочерний класс. Выполнить перегрузку методов конструктора дочернего класса (метод __init__, в который должна
# передаваться переменная — скидка), и перегрузку метода __str__ дочернего класса. В этом методе должна
# пересчитываться цена и возвращаться результат — цена товара со скидкой. Чтобы все работало корректно,
# не забудьте инициализировать дочерний и родительский классы
# (вторая и третья строка после объявления дочернего класса).


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
    def __init__(self, __name, __prise, discount):
        super().__init__(__name, __prise)
        self.discount = discount

    def __str__(self):
        return f'Price with discount - {self.get_price() - self.get_price() / 100 * self.discount}.'

    def get_parent_data(self):
        return f'{self.get_name()} - {self.get_price()}'


car = ItemDiscount('ford', 15000)
car = ItemDiscountReport(car.get_name(), car.get_price(), 10)
print(car)
