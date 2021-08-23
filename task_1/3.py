from random import randint


# Разработать генератор случайных чисел. В функцию передавать начальное и
# конечное число генерации (нуль необходимо исключить). Заполнить этими данными
# список и словарь. Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
# Вывести содержимое созданных списка и словаря.


def my_func(min_rand, max_rand):
    if min_rand == 0 or max_rand <= min_rand:
        return print('Минимальное число не должно равняться 0, первое число должно быть меньше второго.')
    rand_list = [randint(min_rand, max_rand) for _ in range(10)]
    rand_dict = {f"elem_{i + 1}": rand_list[i] for i in range(len(rand_list))}
    print(rand_list, rand_dict)


my_func(2, 1)
my_func(0, 1)
my_func(1, 5)
