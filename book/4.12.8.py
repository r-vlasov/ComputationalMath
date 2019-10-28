from math import *

def function(x):
    return x*exp(-x**2) - 1 / (2 * sqrt(2 * exp(1)))

def der_function(x):
    return exp(-x**2) * (1 - 2 * x**2)

def single_step(x):
    return x - function(x) / der_function(x)


def solver(x):
    x0 = -1
    x1 = x

    while (abs(x0 - x1) >= 0.001):
        x0 = x1
        x1 = single_step(x1)
    return x1

print (abs(solver(1) - solver(0)))