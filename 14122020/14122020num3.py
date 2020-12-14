# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('textnum3', 'r') as text:
    a = []
    b = []
    text = text.read().split('\n')
    for i in text:
        i = i.split()
        if int(i[1]) < 20000:
           b.append(i[0])
        a.append(i[1])
print('Оклад меньше 20000:',b,'средний оклад:', sum(map(int, a)) / len(a))#