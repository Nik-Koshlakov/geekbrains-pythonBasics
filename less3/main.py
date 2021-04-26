# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# task 1
def div_f(a, b):
    return a / b


# task 2
def desc_user(**kwargs):
    return print(f'user {kwargs.get("l_name")} {kwargs.get("f_name")}, '
                 f'brth date {kwargs.get("brth")}, '
                 f'city {kwargs.get("city")}, email {kwargs.get("email")}, '
                 f'phone {kwargs.get("phone")}')


# task 3
def my_func(*args):
    result = sorted(args, reverse=True)
    return result[0] + result[1]


# task 4
def pows_1(x, y):
    i = 2
    res = x
    while i <= -y:
        res = res * x
        i += 1
    return res


def pows_2(x, y):
    return x ** -y


# task 5
def sum_n():
    print('Символ окончания - .')
    flag = False
    sum = 0
    while not flag:
        s = input('введите строку из чисел, разделенных пробелом. '
                  'Возможен ввод символа окончания')
        for c in s.split(' '):
            if c == '.':
                flag = True
                print('Встретился символ окончания')
                break
            else:
                sum += int(c)

        print('current sum: ', sum)

    return sum


# task 6
def int_func(word):
    return str(word).title()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # t1
    a, b = map(int, input('two numbers: ').split(' '))
    _div = div_f(a, b)

    # t2
    desc_user(f_name="I", l_name="II", brth="11/09/94", city="Mscw",
              email="nk@ya.ru", phone="(915)226-41-72")

    # t3
    _sum = my_func(8, 1, 5)

    # t4
    r1 = pows_1(3, -4)
    r2 = pows_1(2, -10)
    r2_2 = pows_2(2, -10)
    r3 = pows_1(2.2, -10)

    # t5
    sum = sum_n()

    # t6
    print(int_func(input('Введите два слова: ')))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
