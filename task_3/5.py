# Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором
# списке часть строковых значений заменить на значения типа example345 (строка+число).
# Далее — усовершенствовать вторую функцию из предыдущего примера (функцию извлечения данных).
# Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
# вывод первого вхождения, вывод всех вхождений. Реализовать замену всех найденных подстрок
# на новое значение и вывод всех подстрок, состоящих из букв и цифр и имеющих пробелы
# только в начале и конце — например, example345.

import os
import random
import re


def read_file(f_path):
    with open(f_path, 'r') as file:
        # Далее — усовершенствовать вторую функцию из предыдущего примера (функцию извлечения данных).
        # Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
        # вывод первого вхождения, вывод всех вхождений.
        context = file.read()
        str_indices = [m.start() for m in re.finditer(" example345 \n", context)]
        print(f'Индекс первого вхождения = {str_indices[0]}, '
              f'индексы последующих вхождений = {str(str_indices[1:]).strip("[]")}.')
    with open(f_path, 'r') as file:
        for line in file:
            # Реализовать замену всех найденных подстрок
            # на новое значение
            if "example345" not in line:
                print("Новое значение.")
                # и вывод всех подстрок, состоящих из букв и цифр и имеющих пробелы
                # только в начале и конце — например, example345.
            if re.match("^[A-Za-z0-9 ]*$", line) and line[0] == ' ' and line[-2] == ' ':
                print(line)


def create_file():
    if os.path.exists('test_file.txt'):
        print(f'test_file.txt already exists')
        raise SystemExit
    else:
        with open('test_file.txt', 'w') as file:
            num_list = [random.randint(1, 10) for _ in range(10)]
            str_list = [random.choice('letters') for _ in range(10)]
            el_list = list(zip(num_list, str_list))
            # Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором
            # списке часть строковых значений заменить на значения типа example345 (строка+число).
            counter = 0
            for el in el_list:
                file.write("%s\n" % ''.join(c for c in str(el) if c.isalpha() or c.isdigit()))
                if counter % 3 == 0:
                    file.write(' example345 \n')  # для выполнения условия последнего задания в строку добавлены
                    # пробелы.
                counter += 1
        read_file(os.path.abspath('test_file.txt'))


create_file()
