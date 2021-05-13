class InputNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def is_number(num):
        return num.isdigit()


def fillingArray():
    arr = []
    print('For stopping input string enter "stop"')
    while True:
        try:
            inp = input('input element - ')
            if inp == 'stop':
                break
            if not InputNumberError.is_number():
                raise InputNumberError('Введенное значение не число')
        except InputNumberError as e:
            print(e)
        else:
            arr.append(inp)
    print(arr)