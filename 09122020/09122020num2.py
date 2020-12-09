spisok = [1, 2, 3, 10, 9, 3, 2, 4]
print("Список:", spisok)
spisok1 = [i for num, i in enumerate(spisok) if spisok[num - 1] < spisok[num]]
print("Новый список:", spisok1)

