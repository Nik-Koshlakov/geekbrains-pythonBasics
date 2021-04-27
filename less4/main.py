import random
from functools import reduce
from itertools import count
from itertools import cycle


def task_2(lst):
    print(lst)
    return [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i - 1]]


def task_3():
    return [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]


def task_4(mass):
    return [mass[i] for i in range(0, len(mass)) if mass.count(mass[i]) == 1]


def task_5():
    def my_func(prev_el, el):
        return prev_el * el

    return reduce(my_func, [i for i in range(100, 1000, 2)])


def task_6():
    def cnt():
        beg = int(input('beginning from number: '))
        for el in count(beg):
            if el == beg + 10:
                break
            else:
                print(el)

    def cycl():
        с = 0
        print('cycle ABC:')
        for el in cycle("ABC"):
            if с > 10:
                break
            print(el)
            с += 1

    cnt()
    cycl()


def task_7():
    def fact(n):
        res = 1
        for j in range(1, n + 1):
            res *= j
            yield res

    print('factorial:')
    for i in fact(4):
        print(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('task 2: ', task_2([random.randint(1, 400) for i in range(0, 12)]))
    print('task 3: ', task_3())
    print('task 4: ', task_4([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]))
    print('task 5: ', task_5())
    task_6()
    task_7()
