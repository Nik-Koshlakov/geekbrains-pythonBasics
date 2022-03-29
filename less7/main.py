from matrix import Matrix

from clothes import Coat
from clothes import Costume
from clothes import Project

from cell import Cell


if __name__ == '__main__':
    # task1
    m1 = Matrix(3, 3, True)
    print("m1")
    print(m1)
    m2 = Matrix(3, 3, True)
    print("m2")
    print(m2)
    print("-----")
    print(m1 + m2)

    # task2
    coat = Coat(13)
    costume = Costume(5)
    project = Project()
    exp = coat.expense()
    project.add_expense(exp)
    project.add_expense(costume.expense())
    project.all_expense()

    # task3
    c1 = Cell(12)
    c2 = Cell(6)
    print(c1.make_order(12))
    print(c1 + c2)
    print(c1 - c2)
    print(c1 * c2)
    print(c1 / c2)






