newnames = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
text = []
with open('textnum4', 'r') as text1:
    content = text1.read().split('\n')
    for i in text1:
        i = i.split(' ', 1)
        text.append(newnames[i[0]] + '  ' + i[1])
    print(text)

with open('textnum4p2.txt', 'w') as file_obj_2:
    file_obj_2.writelines(text)