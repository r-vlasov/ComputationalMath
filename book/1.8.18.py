from math import *


# sin
derivatives = (0, 1, 0, -1)

def sin_taylor_member(number, x):
    iterator = number % 4
    if number != 0:
        return  derivatives[iterator] * (x ** (number - 1)) / factorial(number - 1)
    else:
        return 0
    
def sin_row(count, x):
    i = 0
    row = 0
    while i < count:
        row += sin_taylor_member(i, x)
        i += 1
    return row

def row_less_then_1(x):
    i = 1
    row = sin_row(i, x)
    while (row <= 1):
        i += 1
        row = sin_row(i, x)
    return i

x = 1/2
step = 0.1
while (x <= 1):
    print (row_less_then_1(x))
    x += step
