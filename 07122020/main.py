
def delenie(a,b):
    print(a/b)

k = int(input('Введите первое число = '))
m = int(input('Введите первое число = '))
try:
    delenie(k,m)
except ZeroDivisionError:
    m = 0
    b = 0
finally:
    print('Деление на ноль')

