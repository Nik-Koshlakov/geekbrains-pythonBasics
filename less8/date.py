class DateError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Date:
    d = 0
    m = 0
    y = 0

    @classmethod
    def convertClassMethod(cls, param):  # dd-mm-yyyy
        nms_str = param.split('-')
        d = int(nms_str[0])
        m = int(nms_str[1])
        y = int(nms_str[2])
        print(f'{d} {m} {y}')

    @staticmethod
    def convertStaticMethod(param):
        try:
            d, m, y = param.split('-')
            if int(d) < 1 or int(d) > 31:
                raise DateError("Incorrect number of days")
            if int(m) < 1 or int(m) > 12:
                raise DateError("Incorrect number of months")
        except DateError as e:
            print(e)
        else:
            print("Date format correct")