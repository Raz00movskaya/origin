
class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return 'Данные указаны верно'
                else:
                    return 'Неверно указаны данные'
            else:
                return 'Неверно указаны данные'
        else:
            return 'Неверно указаны данные'

    def __str__(self):
        return f'Текущая дата {Date.extract(self.day_month_year)}'


today = Date('18 - 10 - 2001')
print(today)
print(today.valid(18, 10, 2001))
print(today.extract('18 - 10 - 2001'))
