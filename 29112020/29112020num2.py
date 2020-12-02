a = input("Введите элементы списка через запятую без пробелов: ")
spisok = list((a.split(',')))
for i in range(0, len(spisok), 2):
    if (len(spisok) % 2 != 0) and (i == (len(spisok) - 1)):
        break
    spisok[i], spisok[i+1] = spisok[i+1], spisok[i]
print(spisok)
<<<<<<< HEAD
#
=======
>>>>>>> master
#