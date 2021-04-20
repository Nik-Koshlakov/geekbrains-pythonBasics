import copy
from collections import defaultdict
# This is a sample Python script.

even_list = [2, 'text', 45.3, None, False, (5+6j), True, 9]
odd_list = [2, 'text', 45.3, None, False, (5+6j), 7]


def task_1(result_list):
    print(result_list)
    for el in result_list:
        if type(el) is int:
            print(f'int {el}')
        elif type(el) is float:
            print(f'float {el}')
        elif type(el) is str:
            print(f'str {el}')
        elif el is None:
            print(f'None {el}')
        elif type(el) is bool:
            print(f'bool {el}')
        elif type(el) is complex:
            print(f'complex {el}')


def task_2(list):
    new_list = copy.deepcopy(list)
    len_arr = len(new_list)
    for i in range(0, len_arr, 2):
        if i == len_arr - 1:
            break
        tmp = new_list[i]
        new_list[i] = new_list[i+1]
        new_list[i+1] = tmp
    print(list)
    print(new_list)


def task_3():
    month = input('input month number: ')
    list = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
    dict = {'1':'Январь','2':'Февраль','3':'Март','4':'Апрель','5':'Май',
            '6':'Июнь','7':'Июль','8':'Август','9':'Сентябрь','10':'Октябрь',
            '11':'Ноябрь','12':'Декабрь'}

    print(f'month {list[int(month-1)]} by list')
    print(f'month {dict.get(month)} by dict')

    dict2 = {[12, 1, 2]: 'зима', [3, 4, 5]: 'весна', [6, 7, 8]: 'лето', [9, 10, 11]: 'осень'}
    list2 = ['зима','весна','лето','осень']
    for k in dict2.keys():
        if int(month) in k:
            print(f'time year {dict2.get(k)} by dict')
    # через лист тупо выходит...


def task_4():
    str = input('some... ')
    l = list(str.split(' '))
    for ind, s in enumerate(l):
        print(ind, s[:10]) if len(s) > 10 else print(ind, s)


def task_5():
    my_list = [7, 5, 3, 3, 2]
    n = int(input('add number: '))
    my_list.append(n)
    my_list.sort(reverse=True)
    print(my_list)


def task_6():
    tmp_list = []
    list = [
        (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
        (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
        (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
    ]
    for el in list:
        for e in el:
            if isinstance(e, dict):
                tmp_list.append(e)
    print(tmp_list)
    print('--------')

    result_dictionary = {}
    for i in tmp_list:
        for key, value in i.items():
            result_dictionary.setdefault(key, []).append(value)
    print(result_dictionary)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # task_1(even_list)
    """
    task_2(even_list)
    print('----------')
    task_2(odd_list)
    """
    # task_3()
    # task_4()
    # task_5()
    task_6()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
