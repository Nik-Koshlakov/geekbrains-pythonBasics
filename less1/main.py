from datetime import timedelta
import math
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def task_1():
    a = 1
    b = 'b'
    print(a)
    print(b)
    c = input('input some number: ')
    d = int(c)
    print('число {0}, тип {1}'.format(d, type(d)))



def task_2():
    sec = int(input('Введите секунды: '))
    print('time - ', str(timedelta(seconds=sec)))


def task_3():
    _str = input('Введите число: ')
    n = _str
    nn = _str + _str
    nnn = nn + _str
    print('sum = ', int(n) + int(nn) + int(nnn))


def task_4():
    big = 0
    text = input('Введите целое положительное: ')
    i = 0
    while i < len(text):
        num = int(text[i])
        if num > big:
            big = num
        i += 1
    print('Самое большая цифра {0} в числе {1}'.format(big, text))


def task_5():
    v = float(input('Введите выручку: '))
    i = float(input('Введите издержки: '))
    pr = v - i
    if pr > 0:
        rent = pr / v
        print('Фирма работает в прибыль, рентабельность = ', rent)
        people = int(input('Введите число сотрудников: '))
        pr_1peopl = pr / people
        print('Прибыль на одного сотрудника: ', pr_1peopl)
    else:
        print('Фирма работает в убыток')


def task_6():
    km = float(input('Введите число км в первый день: '))
    day = int(input('Результат на какой день? '))
    i = 1
    while i <= day:
        km = km + km*0.1
        i += 1
        #print(km)
    print('на %d-й день спортсмен достиг результата — не менее %d км' % (day, math.floor(km)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #task_1()
    #task_2()
    #task_3()
    #task_4()
    #task_5()
    task_6()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
