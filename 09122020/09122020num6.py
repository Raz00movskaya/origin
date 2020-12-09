from itertools import count
def firstfunc(a, b):
    for i in count(a):
        if i > b:
            break
        else:
            print(i)
from itertools import cycle
def secondfunc(spisok, d):
    i = 0
    iter = cycle(spisok)
    while i < d:
        print(next(iter))
        i+=1
firstfunc(a = int(input("Стартовое число: ")), b = int(input("До какого результата повторять цикл: ")))
secondfunc(spisok = [1, 2, 3, 1, 5, 8, 9], d = int(input("Сколько раз повторять элементы списка: ")))