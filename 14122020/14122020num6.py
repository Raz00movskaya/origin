hours = {}
with open('textnum6', 'r') as text:
    for i in text:
        a, b, c, d = i.split()
        hours[a] = int(b) + int(c) + int(d)
    print('Общее количество часов по предмету',hours)#