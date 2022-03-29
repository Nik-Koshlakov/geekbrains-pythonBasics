class ZeroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt


class CheckDivision:
    @staticmethod
    def check():
        a, b = input('Input two numbers ').split(' ')
        try:
            if int(b) == 0:
                raise ZeroDiv("Can`t divide by 0")
            print(int(a) / int(b))
        except ZeroDiv as e:
            print(e)
        finally:
            print('Finish execute program')