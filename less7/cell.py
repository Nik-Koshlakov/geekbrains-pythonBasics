class Cell:
    def __init__(self, count):
        self.cell_count = count

    def make_order(self, cell_cnt):
        res = ''
        div = self.cell_count // cell_cnt
        for count in range(div):
            res += '*' * cell_cnt + '\n'
        if self.cell_count % cell_cnt != 0:
            res += '*' * (self.cell_count % cell_cnt)
        return res

    def __add__(self, other):
        return Cell(self.cell_count + other.cell_count)

    def __sub__(self, other):
        if self.cell_count - other.cell_count > 0:
            self.cell_count -= other.cell_count
            return self
        else:
            return "can`t sub"

    def __mul__(self, other):
        return Cell(self.cell_count * other.cell_count)

    def __truediv__(self, other):
        return Cell(self.cell_count // other.cell_count)

    def __str__(self):
        return str(self.cell_count)