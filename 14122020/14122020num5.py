with open('textnum5', 'w+') as text:
    line = input('Введите цифры через пробел: \n')
    text.writelines(line)
    nums = line.split()

print(sum(map(int, nums)))#