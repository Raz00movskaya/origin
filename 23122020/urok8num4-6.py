class Sklad:

    def __init__(self, name, price, quantity, number_of_iterations, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_iterations
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Наименование': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'имя {self.name} цена {self.price} количество {self.quantity}'

    def reception(self):

        try:
            a = input(f'Введите наименование товара: ')
            b = int(input(f'Введите цену товара:  '))
            c = int(input(f'Введите количество товара: '))
            d = {'Модель устройства': a, 'Цена за ед': b, 'Количество': c}
            self.my_unit.update(d)
            self.my_store.append(self.my_unit)
            print(f'Текущий список: \n {self.my_store}')
        except:
            return f'Данные введены некорректно'

        q = input('Для выхода - Выход, продолжение - Enter: ')
        if q == 'Выход' or q == 'выход':
            self.my_store_full.append(self.my_store)
            print(f'Информация о складе: \n {self.my_store_full}')
            return f'Выход'
        else:
            return Sklad.reception(self)

class Printer(Sklad):
    def to_print(self):
        return f'Напечатать {self.numb} раз'

class Scanner(Sklad):
    def to_scan(self):
        return f'Отсканировать {self.numb} раз'

class Copier(Sklad):
    def to_copier(self):
        return f'Скопировать {self.numb} раз'

printer = Printer('Printer', 2000, 5, 5)
copier = Copier('Copier', 1500, 1, 5)
print(copier.reception())
print(printer.to_print())
print(copier.to_copier())
