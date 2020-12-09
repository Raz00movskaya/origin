from functools import reduce

def my_func(prev_el, el):
    return prev_el + el

spisok = [i for i in range(99, 1001) if i % 2 == 0]
spisok1 = reduce(my_func, [i for i in range(99, 1001) if i % 2 == 0])

print("Список:",spisok)
print("Сумма элементов:",spisok1)