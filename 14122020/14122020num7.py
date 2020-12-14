import json
a = {}
b = {}
c = 0
d = 0
i = 0
with open('textnum7', 'r') as file:
    for line in file:
        n, f, e, da = line.split()
        a[n] = int(e) - int(da)
        if a.setdefault(n) >= 0:
            c = c + a.setdefault(n)
            i += 1
    if i != 0:
        d = c / i
        print('Прибыль средняя',d)
    else:
        print('Прибыль средняя - отсутсвует. Все работают в убыток')
    b = {'средняя прибыль': round(d)}
    a.update(b)
    print('Прибыль каждой компании', a)
with open('textnum7.json', 'w') as write_js:
    json.dump(a, write_js)
    js_str = json.dumps(a)
    print('Создан файл с расширением json со следующим содержимым:',js_str)#