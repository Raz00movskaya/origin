def my_sum ():
    result = 0
    exit = False
    while exit == False:
        a = input('Введите свои числа через пробел, для выхода - # : ').split()
        res = 0
        for i in range(len(a)):
            if a[i] == '#' or a[i] == '#':
                exit = True
                break
            else:#
                res = res + int(a[i])
        result = result + res
        print('Сумма на данный момент:', result)
    print('Итоговая сумма:',result)
my_sum()