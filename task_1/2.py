# def print_directory_contents(sPath):
#     """
#     Функция принимает имя каталога и распечатывает его содержимое
#     в виде «путь и имя файла», а также любые другие
#     файлы во вложенных каталогах.
#
#     Эта функция подобна os.walk. Использовать функцию os.walk
#     нельзя. Данная задача показывает ваше умение работать с
#     вложенными структурами.
#     """
#     # заполните далее

import os


def print_directory_contents(dir_path):
    dir_list = os.listdir(path=dir_path)
    for el in dir_list:
        el_path = os.path.join(f"{dir_path}{el}\\")
        if os.path.isdir(el_path):
            print(f"Путь: {el_path}, содержимое: {os.listdir(path=el_path)}")
            print_directory_contents(el_path)


# print(print_directory_contents("C:\\"))
print_directory_contents("C:\\Users\\Pavilion\\Documents\\Geek_brains\\")
