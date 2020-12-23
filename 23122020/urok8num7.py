class ComplexNumber:#
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма первого и второго = ')
        return f'c = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение первого и второго = ')
        return f'c = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'c = {self.a} + {self.b} * i'

c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(3, -4)
print(c1)
print(c1 + c2)
print(c1 * c2)