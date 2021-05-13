from random import randrange
from fillingArray import InputNumberError


class OfficeEquip:
    def __init__(self, type, length, width, height, portable=False):
        self.type = type
        self.length = length
        self.width = width
        self.height = height
        self.portable = portable

    def toDict(self):
        d = dict()
        d['type'] = self.type
        d['length'] = self.length
        d['width'] = self.width
        d['height'] = self.height
        d['portable'] = self.portable
        return d


class Printer(OfficeEquip):
    def __init__(self, is_laser, length, width, height, portable=False):
        super().__init__(Printer.__name__, length, width, height, portable)
        self.isLaser = is_laser

    def toDict(self):
        d = super().toDict()
        d['isLaser'] = self.isLaser
        return d


class Scanner(OfficeEquip):
    def __init__(self, is_wifi, length, width, height, portable=False):
        super().__init__(Scanner.__name__, length, width, height, portable)
        self.isWifi = is_wifi

    def toDict(self):
        d = super().toDict()
        d['isWifi'] = self.isWifi
        return d


class Xerox(OfficeEquip):
    def __init__(self, is_color, length, width, height, portable=False):
        super().__init__(Xerox.__name__, length, width, height, portable)
        self.isColor = is_color

    def toDict(self):
        d = super().toDict()
        d['isColor'] = self.isColor
        return d


class StorageOfficeEquip:
    _storageOfficeEquip = []
    _divisionEquip = []
    __division = ['div1', 'div2', 'div3']

    @staticmethod
    def __str2bool(v):
        return v.lower() in ("yes", "y", "true", "t", "1")

    @staticmethod
    def __checkNumber(*arr):
        if not InputNumberError.is_number(arr[0]) \
                or not InputNumberError.is_number(arr[1]) \
                or not InputNumberError.is_number(arr[2]):
            raise InputNumberError('Размерность введена некорректно')

    @staticmethod
    def __checkBool(*arr):
        if not StorageOfficeEquip.__str2bool(arr[0]) or not StorageOfficeEquip.__str2bool(arr[1]):
            raise ValueError('Булево значение введено неверно')

    def userInput(self):
        print('For stopping input string enter "stop"')
        while True:
            try:
                type_equip = input('input type of equip - ')
                if type == 'stop':
                    break
                if type_equip.lower() == 'printer':
                    data = input('Input parameters of equip (is laser? length, width, height, portable): ')
                    self.__checkNumber(data[1], data[2], data[3])
                    self.__checkBool(data[0], data[3])
                    eq = Printer(data[0], Printer.__name__, data[1], data[2], self.__str2bool(data[3]))
                if type_equip.lower() == 'scanner':
                    data = input('Input parameters of equip (is wi-fi? length, width, height, portable): ')
                    self.__checkNumber(data[1], data[2], data[3])
                    self.__checkBool(data[0], data[3])
                    eq = Scanner(data[0], Scanner.__name__, data[1], data[2], self.__str2bool(data[3]))
                if type_equip.lower() == 'xerox':
                    data = input('Input parameters of equip (is color? length, width, height, portable): ')
                    self.__checkNumber(data[1], data[2], data[3])
                    self.__checkBool(data[0], data[3])
                    eq = Xerox(data[0], Xerox.__name__, data[1], data[2], self.__str2bool(data[3]))
                """if not InputNumberError.is_number(data[1]) \
                        or not InputNumberError.is_number(data[2]) \
                        or not InputNumberError.is_number(data[3]):
                    raise InputNumberError('Размерность введена некорректно')
                if not self.__str2bool(data[0]) or not self.__str2bool(data[6]):
                    raise ValueError('Булево значение введено неверно')"""
            except InputNumberError as e:
                print(e)
            except ValueError as e:
                print(e)
            else:
                self.addToStorage(eq)

    def addToStorage(self, equip):
        find = False
        for eq in self._storageOfficeEquip:
            if eq['name'] == equip.type:
                eq['count'] += eq['count']
                eq['equip'].append(equip.toDict())
                find = True
        if not find:
            self._storageOfficeEquip.append(
                {"name": equip.type, "count": 1, "equip": [equip.toDict()]})

    def receiptEquip(self):
        if len(self._storageOfficeEquip) == 0:
            print('На складе пусто')
        else:
            d = self.__division[randrange(len(self.__division))]
            st_equip = self._storageOfficeEquip.pop(0)
            is_exist = False
            for div in self._divisionEquip:
                if list(div.keys())[0] == d:
                    div[d].append(st_equip)
                    is_exist = True
            if not is_exist:
                dc = dict()
                dc.setdefault(d, []).append(st_equip)
                self._divisionEquip.append(dc)

    def printDivisionEquip(self):
        for div in self._divisionEquip:
            for key, values in div.items():
                print(key)
                for val in values:
                    print(f'\t{val}')