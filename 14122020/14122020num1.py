text = open('text.txt', 'w')
stroka = input('Начать ввод данных')
while stroka != "":
    stroka = input('Введите строку, для выхода - пустую: \n')
    text.writelines(stroka)
text.close()
#