# 4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
# Если файл с таким именем уже существует, выводим соответствующее сообщение. Необходимо открыть файл и подготовить
# два списка: с текстовой и числовой информацией. Для создания списков использовать генераторы. Применить к спискам
# функцию zip(). Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
# чтобы каждая строка файла содержала текстовое и числовое значение. Вызвать вторую функцию. В нее должна
# передаваться ссылка на созданный файл. Во второй функции необходимо реализовать открытие файла и простой
# построчный вывод содержимого. Вся программа должна запускаться по вызову первой функции.
import os
import random


# Во второй функции необходимо реализовать открытие файла и простой
# построчный вывод содержимого.
def read_file(f_path):
    with open(f_path, 'r') as file:
        print(file.read())


def create_file():
    # В первой функции должен создаваться простой текстовый файл.
    # Если файл с таким именем уже существует, выводим соответствующее сообщение.
    if os.path.exists('test_file.txt'):
        print(f'test_file.txt already exists')
        raise SystemExit
    else:
        with open('test_file.txt', 'w') as file:
            # Необходимо открыть файл и подготовить
            # два списка: с текстовой и числовой информацией. Для создания списков использовать генераторы.
            num_list = [random.randint(1, 10) for _ in range(10)]
            str_list = [random.choice('letters') for _ in range(10)]
            #  Применить к спискам функцию zip().
            el_list = list(zip(num_list, str_list))
            # Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
            # чтобы каждая строка файла содержала текстовое и числовое значение.
            for el in el_list:
                file.write("%s\n" % ''.join(c for c in str(el) if c.isalpha() or c.isdigit()))
            # Вызвать вторую функцию. В нее должна
            # передаваться ссылка на созданный файл.
        read_file(os.path.abspath('test_file.txt'))


#  Вся программа должна запускаться по вызову первой функции.
create_file()
