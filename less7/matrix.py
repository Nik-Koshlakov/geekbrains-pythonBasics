import random


class Matrix:
    def __init__(self, matr):
        self.matrix = matr
        self.row = len(matr)
        self.col = len(matr[0])

    def __init__(self, n, m, rand=False):
        self.row = n
        self.col = m
        if rand:
            self.matrix = [[random.randrange(0, 10) for j in range(self.col)] for i in range(self.row)]
        else:
            self.matrix = [[0] * m for i in range(n)]

    def __str__(self):
        for row in range(self.row):
            print(self.matrix[row])
        return ""

    def __add__(self, other):
        # var 1
        """m = Matrix(self.row, self.col)
        for row in range(self.row):
            for col in range(self.col):
                m.matrix[row][col] = self.matrix[row][col] + other.matrix[row][col]
        return m"""
        # var 2
        m = Matrix(self.row, self.col)
        for row in range(self.row):
            m.matrix[row] = [x + y for x, y in zip(self.matrix[row], other.matrix[row])]
        return m