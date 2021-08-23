# Написать программу «Банковский депозит». Она должна состоять из функции и ее вызова с аргументами.
# Клиент банка делает депозит на определенный срок. В зависимости от суммы и срока вклада определяется
# процентная ставка:
# 1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых).
# 10001–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых).
# 100001–1000000 руб(6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых).
# Необходимо написать функцию,
# в которую будут передаваться параметры: сумма вклада и срок вклада. Каждый из трех банковских продуктов
# должен быть представлен в виде словаря с ключами (begin_sum, end_sum, 6, 12, 24). Ключам соответствуют
# значения начала и конца диапазона суммы вклада и значения процентной ставки для каждого срока.
# В функции необходимо проверять принадлежность суммы вклада к одному из диапазонов и выполнять расчет
# по нужной процентной ставке. Функция возвращает сумму вклада на конец срока.


# def calc_end_sum(dep_term, dep_default_dict):
#     percent_for_months = dep_default_dict.get(str(dep_term)) / 12 * dep_term
#     begin_sum = dep_default_dict.get('begin_sum')
#     end_sum = dep_default_dict.get('begin_sum') + (begin_sum / 100 * percent_for_months)
#     print(f'Cумма Вашего вклада на конец срока будет сотавлять {end_sum} руб.')
#
#
# def calc_deposit(begin_sum, dep_term):
#     if begin_sum >= 100001:
#         dep_default_dict = {
#             "begin_sum": begin_sum,
#             "end_sum": None,
#             "6": 7,
#             "12": 8,
#             "18": 7.5
#         }
#         calc_end_sum(dep_term, dep_default_dict)
#     elif begin_sum >= 10001:
#         dep_default_dict = {
#             "begin_sum": begin_sum,
#             "end_sum": None,
#             "6": 6,
#             "12": 7,
#             "18": 6.5
#         }
#         calc_end_sum(dep_term, dep_default_dict)
#     elif begin_sum >= 1000:
#         dep_default_dict = {
#             "begin_sum": begin_sum,
#             "end_sum": None,
#             "6": 5,
#             "12": 6,
#             "18": 5
#         }
#         calc_end_sum(dep_term, dep_default_dict)
#     else:
#         print("Сумма депозита не может быть меньше 1000.")
#
#
# calc_deposit(1000, 6)
# calc_deposit(1000, 12)
# calc_deposit(1000, 18)
# calc_deposit(10001, 6)
# calc_deposit(10001, 12)
# calc_deposit(10001, 18)
# calc_deposit(100001, 6)
# calc_deposit(100001, 12)
# calc_deposit(100001, 18)


def calc_deposit_2(begin_sum, dep_term):
    dep_default_dict = {
        "begin_sum": begin_sum,
        "end_sum": None,
        "6": [5, 6, 7],
        "12": [6, 7, 8],
        "18": [5, 6.5, 7.5]
    }
    if begin_sum >= 100001:
        index = 2
    elif begin_sum >= 10001:
        index = 1
    elif begin_sum >= 1000:
        index = 0
    else:
        print("Сумма депозита не может быть меньше 1000.")
        return
    valid_percent_list = dep_default_dict.get(str(dep_term))
    valid_percent_item = valid_percent_list[index]
    percents_for_months = valid_percent_item / 12 * int(dep_term)
    end_sum = begin_sum + (begin_sum / 100 * percents_for_months)
    print(f'Cумма Вашего вклада на конец срока будет сотавлять {end_sum} руб.')


calc_deposit_2(999, 6)
calc_deposit_2(1000, 6)
calc_deposit_2(1000, 12)
calc_deposit_2(1000, 18)
calc_deposit_2(10001, 6)
calc_deposit_2(10001, 12)
calc_deposit_2(10001, 18)
calc_deposit_2(100001, 6)
calc_deposit_2(100001, 12)
calc_deposit_2(100001, 18)
