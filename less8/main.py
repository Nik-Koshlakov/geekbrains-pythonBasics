from date import Date
from checkDivision import CheckDivision
from fillingArray import *
from storageOfficeEquip import *
from cmplx import Cmplx


if __name__ == '__main__':
    # task 1
    Date.convertStaticMethod('10-10-2020')
    Date.convertClassMethod('10-10-2020')

    # task 2
    CheckDivision.check()
    CheckDivision.check()

    # task 3
    fillingArray()

    # task 4-6
    pr = Printer(True, 10, 10, 10)
    sc1 = Scanner(True, 10, 15, 5, True)
    sc2 = Scanner(False, 10, 20, 7, True)
    xx = Xerox(True, 15, 15, 15)
    storage = StorageOfficeEquip()
    storage.addToStorage(pr)
    storage.addToStorage(sc1)
    storage.addToStorage(sc2)
    storage.addToStorage(xx)
    storage.receiptEquip()
    storage.receiptEquip()

    storage.printDivisionEquip()

    # task 7
    Cmplx.test()