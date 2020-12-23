
class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def divide_by_null(a, b):
        try:
            return (a / b)#
        except:
            return 'Деление на ноль недопустимо'

print(Division.divide_by_null(input('Введите делимое:'), input('Введите делитель: ')))
