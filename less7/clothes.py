from abc import ABC, abstractmethod


class Cloth:
    def __init__(self):
        self.__V = None
        self.__H = None

    def __init__(self, V, H):
        self.__V = V
        self.__H = H

    @property
    def V(self):
        return self.__V

    @V.setter
    def V(self, V):
        self.__V = V

    @property
    def H(self):
        return self.__H

    @H.setter
    def H(self, H):
        self.__H = H


class ClothesAbstract(ABC):
    @abstractmethod
    def expense(self):
        pass


class Coat(Cloth, ClothesAbstract):
    def __init__(self, V):
        self.__V = V
        self.name = "Пальто"

    def expense(self):
        return self.__V/6.5 + 0.5


class Costume(ClothesAbstract):
    def __init__(self, H):
        self.__H = H
        self.name = "Костюм"

    def expense(self):
        return 2 * self.__H + 0.3


class Project:
    def __init__(self):
        self.total_expense = []

    def add_expense(self, type_clothing_expense):
        self.total_expense.append(type_clothing_expense)

    def all_expense(self):
        sum = 0
        for exp in self.total_expense:
            sum += exp
        print(f'Общий расход ткани {sum}м')