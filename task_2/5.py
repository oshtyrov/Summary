# Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport
# на два класса. Инициализировать классы необязательно. Внутри каждого поместить функцию get_info,
# которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены. Далее реализовать
# выполнение каждой из функции тремя способами.


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReportA(ItemDiscount):
    def get_info(self):
        return f'{self.get_name()}'


class ItemDiscountReportB(ItemDiscount):
    def get_info(self):
        return f'{self.get_price()}'


car = ItemDiscount('ford', 15000)
print(ItemDiscountReportA.get_info(car))
print(ItemDiscountReportB.get_info(car))

car.get_info = ItemDiscountReportA.get_info(car)
print(car.get_info)
car.get_info = ItemDiscountReportB.get_info(car)
print(car.get_info)

car.get_info = f"{ItemDiscountReportA.get_info(car)} - {ItemDiscountReportB.get_info(car)}"
print(car.get_info)
