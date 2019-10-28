import numpy as np
from numpy import *
import matplotlib.pyplot as plt 

population = np.array([92228496, 106021537, 123202624,
132154569, 151325798, 179323175,
203535805, 226545805, 248709837, 281421906])
years = np.array ([1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000])

def coeficiente(x,y) :
    x.astype(float)
    y.astype(float)
    n = len(x)
    F = zeros((n,n), dtype=float)
    b = zeros(n) 
    for i in range(0,n):
        F[i,0]=y[i]



    for j in range(1, n):
        for i in range(j,n):
            F[i,j] = float(F[i,j-1]-F[i-1,j-1])/float(x[i]-x[i-j])


    for i in range(0,n):
        b[i] = F[i,i]

    return np.array(b) # return an array of coefficient

def Eval(a, x, r):
    x.astype(float)
    n = len( a ) - 1
    temp = a[n]
    for i in range( n - 1, -1, -1 ):
        temp = temp * ( r - x[i] ) + a[i]
    return temp # return the y_value interpolation  return p

def func(x):
    return Eval(coeficiente(years, population), years, x)

def figure():
    y = lambda x: func(x)
    fig = plt.subplots
    x = np.linspace(1910, 2010, 1000)
    plt.plot(x, y(x))
    plt.show()

figure()