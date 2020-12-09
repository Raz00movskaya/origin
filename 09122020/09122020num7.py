from itertools import count
from math import factorial

def func():
    for i in count(1):
        yield factorial(i)

generator = func()
x = 0
for i in generator:
    if x < 15:
        print(i)
        x += 1
    else:
        break