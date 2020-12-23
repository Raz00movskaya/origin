class Proverka:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
#
        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                exit1 = input('Попробовать еще раз? Да или Нет: ')

                if exit1 == 'Да' or exit1 == 'да':
                    print(try_except.my_input())
                elif exit1 == 'Нет' or exit1 == 'нет':
                    return 'Вы вышли'
                else:
                    return 'Вы вышли'

try_except = Proverka(1)
print(try_except.my_input())