
def vozv(x,y):
    print(x**y)

def vozv2(x,y):
    res = 1
    for i in range(y):
        res *= x
    print(res)
#
vozv(int(input('Введите первое число = ')), int(input('Введите второе число = ')))
vozv2(int(input('Введите первое число = ')), int(input('Введите второе число = ')))