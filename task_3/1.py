# Написать программу, которая будет содержать функцию для получения имени файла из полного
# пути до него. При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
# В функции необходимо реализовать поиск полного пути по имени файла, а затем «выделение» из этого пути имени
# файла (без расширения).

import os
import win32api

file_name = 'find_me.txt'


# disk_d_path = "D:\\"


def local_disk_search(d_path, f_name):
    dir_list = os.listdir(path=d_path)
    for el in dir_list:
        el_path = os.path.join(f"{d_path}{el}\\")
        if el == f_name:
            print(f"Путь: {el_path}, имя файла: {el.split('.')[0]}")
            raise SystemExit  # поиск проходит до нахождения первого файла с заданным названием.
        if os.path.isdir(el_path):
            local_disk_search(el_path, f_name)


def search(f_name):
    # local_disk_search(disk_d_path, f_name)
    local_disks = win32api.GetLogicalDriveStrings()
    local_disks = local_disks.split('\000')[:-1]
    for disk in local_disks:
        local_disk_search(disk, f_name)


# При поиске на диске С получаю PermissionError: [WinError 5] Отказано в доступе: 'C:\\Documents and Settings\\'.
# Во время тестов поиска на других дисках программа отрабатывает коректно.
# Для поиска на диске С Необходимо запускать скрипт от имени администратора через командную строку.

search(file_name)
