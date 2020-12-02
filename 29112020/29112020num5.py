rating = [7, 5, 3, 3, 2]
menu = int(input("Введите число рейтинга, 10101 для выхода: "))
while menu != 10101:
    for i in range(len(rating)):
        if rating[i] == menu:
            rating.insert(i + 1, menu)
            break
        elif rating[0] < menu:
            rating.insert(0, menu)
        elif rating[-1] > menu:
            rating.append(menu)
        elif rating[i] > menu and rating[i + 1] < menu:
            rating.insert(i + 1, menu)
    print(rating)
    menu = int(input("Введите число "))
<<<<<<< HEAD
    #
=======
>>>>>>> master
    #