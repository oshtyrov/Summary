# Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна
# передаваться фиксированная ежемесячная сумма пополнения вклада. Необходимо в главной функции
# реализовать вложенную функцию подсчета процентов для пополняемой суммы. Примем, что клиент вносит
# средства в последний день каждого месяца, кроме первого и последнего. Например, при сроке вклада в
# 6 месяцев пополнение происходит в течение 4 месяцев. Вложенная функция возвращает сумму дополнительно
# внесенных средств (с процентами), а главная функция — общую сумму по вкладу на конец периода.


def calc_top_up_amount(valid_percent_item, dep_term, top_up_amount):
    sum_top_up_amount = 0
    percent_for_month = valid_percent_item / 12
    for i in range(dep_term - 2):
        sum_top_up_amount += top_up_amount
        sum_top_up_amount += sum_top_up_amount / 100 * percent_for_month
    return sum_top_up_amount


def calc_deposit(begin_sum, dep_term, top_up_amount):
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
    end_sum = begin_sum + (begin_sum / 100 * percents_for_months) + calc_top_up_amount(valid_percent_item, dep_term,
                                                                                       top_up_amount)
    print(f'Cумма Вашего вклада на конец срока будет сотавлять {round(end_sum, 3)} руб.')


calc_deposit(10001, 6, 200)
