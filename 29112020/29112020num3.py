month = int(input('Введите номер месяца: '))
#month_list = [1, "Зима", 2, "Зима", 3, "Весна", 4, "Весна", 5, "Весна", 6, "Лето", 7, "Лето", 8, "Лето", 9, "Осень", 10, "Осень", 11, "Осень", 12, "Зима"]
#for i in range(0, len(month_list)):
#    if month == month_list[i]:
#        print(month_list[i+1])


month_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
if month == 12 or month <=2:
    print(month_dict.get(1))
elif month<=5:
    print(month_dict.get(2))
elif month<=8:
    print(month_dict.get(3))
elif month<=11:
    print(month_dict.get(4))
#