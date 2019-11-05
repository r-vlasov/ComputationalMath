from scipy import interpolate

def f(x):
    x_points = ([1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000])
    y_points = ([92228496, 106021537, 123202624,
132154569, 151325798, 179323175,
203535805, 226545805, 248709837, 281421906])

    tck = interpolate.splrep(x_points, y_points)
    return interpolate.splev(x, tck)


import numpy as np
from numpy import *
import matplotlib.pyplot as plt  

def figure():
    y = lambda x: f(x)
    fig = plt.subplots
    x = np.linspace(1910, 2010, 1000)
    plt.plot(x, y(x))
    plt.show()

print(f(2010))
figure()
print(f(2010))
