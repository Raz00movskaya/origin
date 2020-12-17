spisok = []
i = int(input('Сколько записей структуры вы хотите добавить: '))
nazvan = []
cen = []
kolv = []
ed = []
for j in range(0,i):
    nazvanie = input('Введите название товара: ')
    nazvan.append(nazvanie)
    cena = input('Введите цену товара: ')
    cen.append(cena)
    kolvo = input('Введите количество товара: ')
    kolv.append(kolvo)
    edizm = input('Введите единицу измерения товара: ')
    ed.append(edizm)
    kortezh = (j, {'Название':nazvanie , 'Цена':cena, 'Количество':kolvo, 'Единица измерения':edizm})
    spisok.append(kortezh)

slovar = {'Название':[nazvan],'Цена':[cen],'Количество':[kolv],'Единица измерения':[ed]}
print(slovar)
#