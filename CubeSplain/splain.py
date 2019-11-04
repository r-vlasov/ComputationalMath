import matplotlib.pyplot as plt
from matplotlib import mlab

class SplineTuple:
    def __init__(self, a, b, c, d, x):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.x = x
 
def BuildSpline(x, y, n):
    splines = [SplineTuple(0, 0, 0, 0, 0) for _ in range(0, n)]
    for i in range(0, n):
        splines[i].x = x[i]
        splines[i].a = y[i]
    
    splines[0].c = splines[n - 1].c = 0.0
    
    alpha = [0.0 for _ in range(0, n - 1)]
    beta  = [0.0 for _ in range(0, n - 1)]
 
    for i in range(1, n - 1):
        hi  = x[i] - x[i - 1] # general case
        hi1 = x[i + 1] - x[i] # general case
        A = hi
        C = 2.0 * (hi + hi1)
        B = hi1
        F = 6.0 * ((y[i + 1] - y[i]) / hi1 - (y[i] - y[i - 1]) / hi)
        z = (A * alpha[i - 1] + C)
        alpha[i] = -B / z
        beta[i] = (F - A * beta[i - 1]) / z
  
 
    for i in range(n - 2, 0, -1):
        splines[i].c = alpha[i] * splines[i + 1].c + beta[i]
    
    for i in range(n - 1, 0, -1):
        hi = x[i] - x[i - 1]
        splines[i].d = (splines[i].c - splines[i - 1].c) / hi
        splines[i].b = hi * (2.0 * splines[i].c + splines[i - 1].c) / 6.0 + (y[i] - y[i - 1]) / hi
    return splines
 
 
def Interpolate(splines, x):
    if not splines:
        return None
    
    n = len(splines)
    s = SplineTuple(0, 0, 0, 0, 0)
    
    if x <= splines[0].x:
        s = splines[0]
    elif x >= splines[n - 1].x: 
        s = splines[n - 1]
    else: 
        i = 0
        j = n - 1
        while i + 1 < j:
            k = i + (j - i) // 2
            if x <= splines[k].x:
                j = k
            else:
                i = k
        s = splines[j]
    
    dx = x - s.x
    return s.a + s.b * dx + s.c / 2.0 * dx**2 + s.d / 6.0 * dx**3 
    
x = mlab.frange(0, 3, 0.2)
y = [
    0, 1.09351, -0.47812, -0.0620008, 0.965999, -0.960168, -1.42145, -0.328504, 
    -1.88517, -2.36515, 2.33714, -0.684984, -0.695581, 1.9807, 2.44249, 3.48356
]
spline = BuildSpline(x, y, len(x))

plt.scatter(x, y)
plt.plot(x, y)

x = mlab.frange(0, 3, 0.01)
plt.plot(x, [Interpolate(spline, x) for x in x])
plt.show()
#============================================
 
