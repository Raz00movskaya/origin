class Material:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return self.width / 6.5 + 0.5

    def get_square_j(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str('Общая площадь ткани: \n', (self.width / 6.5 + 0.5) + (self.height * 2 + 0.3))

class Coat(Material):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return 'Площадь ткани для пальто: ', self.square_c

class Costume(Material):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return 'Площадь ткани для костюма:', self.square_j

coat = Coat(1, 164)
costume = Costume(2, 155)
print(coat)
print(costume)
print(coat.get_sq_full)
print(costume.get_sq_full)
print(costume.get_square_c())
print(costume.get_square_j())