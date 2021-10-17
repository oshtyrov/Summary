# 3. Создать два списка с различным количеством элементов. В первом должны быть записаны
# ключи, во втором — значения. Необходимо написать функцию, создающую из данных ключей и
# значений словарь. Если ключу не хватает значения, в словаре для него должно сохраняться
# значение None. Значения, которым не хватило ключей, необходимо отбросить.

keys_list = ['key_0', 'key_1', 'key_2', 'key_3', 'key_4', 'key_5', 'key_6', 'key_7']
keys_list_2 = ['key_0', 'key_1', 'key_2', 'key_3']
values_list = ['val_0', 10, True, False, 10.2, 'qwerty']


def dict_gen_2(k_l, v_l):
    len_kl = len(k_l)
    len_vl = len(v_l)
    if len_kl > len_vl:
        v_l += [None for _ in range(len_kl - len_vl)]
    return dict(zip(k_l, v_l))


print(dict_gen_2(keys_list, values_list))
print(dict_gen_2(keys_list_2, values_list))


# def dict_gen(k_l, v_l):
#     len_kl = len(k_l)
#     len_vl = len(v_l)
#     if len_vl >= len_kl:
#         return {k_l[i]: v_l[i] for i in range(len(k_l))}
#     else:
#         v_l += [None for i in range(len_kl - len_vl)]
#         return {k_l[i]: v_l[i] for i in range(len(k_l))}
#
#
# print(dict_gen(keys_list, values_list))
