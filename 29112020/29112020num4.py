slova = input('Введите слова через пробел: ')
razn_slova = (slova.split(' '))
for i in range(0, len(razn_slova)):
    print((i+1), 'слово:', (razn_slova[i])[0:10:])
#