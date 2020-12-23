class Cell:
    def __init__(self, a):
        self.a = int(a)

    def __str__(self):
        return 'Результат операции:', self.a * "*"

    def __add__(self, other):
        self.result = Cell(self.a + other.quantity)
        return Cell(self.a + other.quantity)

    def __sub__(self, other):
        return self.a - other.quantity if (self.a - other.quantity) > 0 else print('Отрицательно')

        return Cell(int(self.a - other.a))

    def __mul__(self, other):
        self.result = Cell(int(self.a * other.a))
        return Cell(int(self.a * other.a))

    def __truediv__(self, other):
        self.result = Cell(round(self.a // other.a))
        return Cell(round(self.a // other.a))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.a / cells_in_row)):
            row += "*" * cells_in_row , '\\n'
        row += "*" * (self.a % cells_in_row)
        return row

cell1 = Cell(2)
cell2 = Cell(12)
print(cell1)
print(cell1 + cell2)
print(cell2 - cell1)
print(cell2.make_order(5))
print(cell1.make_order(6))
print(cell1 / cell2)