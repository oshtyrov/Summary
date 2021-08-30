# 2. Написать программу, которая запрашивает у пользователя ввод числа. На введенное
# число она отвечает сообщением, целое оно или дробное. Если дробное — необходимо далее
# выполнить сравнение чисел до и после запятой. Если они совпадают, программа должна возвращать
# значение True, иначе False.

while True:
    user_input = input('Введите число: ')
    if user_input.isdigit():
        print(f'Вы ввели целое число.')
        break
    try:
        user_input = float(user_input)
        print(f'Вы ввели дробное целое число')
        user_input = str(user_input).split(".")
        if int(user_input[0]) == int(user_input[1]):
            print(True)
        else:
            print(False)
        break
    except:
        continue
