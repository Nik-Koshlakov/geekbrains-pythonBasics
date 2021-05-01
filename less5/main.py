import random
import json


def task_1():
    with open('task1.txt', 'w') as file:
        while True:
            s = input('input some string: ')
            if not s:
                break
            else:
                file.write(s + "\n")


def task_2():
    with open('task2.txt', 'r') as file:
        lines = file.readlines()
        print('number of lines: ', len(lines))
        for i in range(0, len(lines)):
            print(f'word count: {len(lines[i].split(" "))}, in line: {i + 1}')


def task_3():
    with open('task3.txt', 'r', encoding="utf-8") as file:
        cnt = 0
        res = 0
        for l in file:
            name, zp = l.split(' ')
            if float(zp) < 20000:
                print('Employee: ', name)
                cnt += 1
                res += float(zp)
        print('middle zp: ', res / cnt)


def task_4():
    with open('task4_out.txt', 'w', encoding="utf-8") as file_w:
        with open('task4.txt', 'r', encoding="utf-8") as file_r:
            for str in file_r:
                if str.find('One') > -1:
                    file_w.write(str.replace("One", "Один"))
                elif str.find('Two') > -1:
                    file_w.write(str.replace("Two", "Два"))
                elif str.find('Three') > -1:
                    file_w.write(str.replace("Three", "Три"))
                elif str.find('Four') > -1:
                    file_w.write(str.replace("Four", "Четыре"))


def task_5():
    with open('task5.txt', 'w') as file_in:
        for i in range(10):
            if i != 9:
                file_in.write(str(random.randint(0, 100)) + ' ')
            else:
                file_in.write(str(random.randint(0, 100)))

    with open('task5.txt', 'r') as file:
        arr_number = file.read().split(' ')
        sum = 0
        for i in arr_number:
            sum += int(i)
        print(f'Arr: {arr_number}, Sum = {sum}')


def task_6():
    with open('task6.txt', 'r', encoding="utf-8") as file:
        arr_str = file.readlines()
        my_d = dict()
        for s in arr_str:
            sum = 0
            arr = s.split(' ')
            for i in range(1, len(arr)):
                if arr[i] == '—':
                    continue
                _s1 = arr[i]
                idx_kv = _s1.index('(')
                sum += int(_s1[:idx_kv])
            my_d[arr[0]] = sum
        print(my_d)


def task_7():
    with open('task7.txt', 'r', encoding="utf-8") as file:
        arr_str = file.readlines()
        my_d = dict()
        cnt_avg = 0
        avg = 0
        for s in arr_str:
            arr = s.split(' ')
            calc = int(arr[2]) - int(arr[3])
            my_d[arr[0]] = calc
            if calc > 0:
                avg += calc
                cnt_avg += 1
        result = [] + [my_d]
        result.append(dict(average_profit=avg))

        with open("task7_out.json", "w") as write_f:
            json.dump(result, write_f)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    task_7()
