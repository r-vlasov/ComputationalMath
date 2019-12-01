from math import *

class Settings_sin:
    def __init__(self, t_min=0, t_max=1):
        self.ders = (0, 1, 0, -1)
        self.dt = 0.001
        self.t_min = t_min
        self.t_max = t_max

    def solve_in(self, x, n):
        i = 0
        sum = 0
        while (i <= n):
            sum += self.ders[i%4]*x**i/factorial(i)
            i += 1
        return sum       

    def def_n(self):
        # because first derivative > 0
        cur_x = self.t_min
        n = []
        while (cur_x < self.t_max):
            cur_n = 1
            while(abs(self.solve_in(cur_x + self.dt, cur_n) - sin(cur_x)) >= self.dt):
                cur_n += 1
            n.append(cur_n)
            cur_x += self.dt
        return max(n)


class Settings_exp:
    def __init__(self, t_min=0, t_max=1):
        self.dt = 0.001
        self.t_min = t_min
        self.t_max = t_max

    def solve_in(self, x, n):
        i = 0
        sum = 0
        while (i <= n):
            sum += x**i/factorial(i)
            i += 1
        return sum 

    def def_n(self):
        # because first derivative > 0
        cur_x = self.t_min + self.dt
        n = []
        while (cur_x < self.t_max):
            cur_n = 1
            while(self.solve_in(cur_x + self.dt, cur_n) - exp(cur_x + self.dt) > self.dt):
                cur_n += 1
            n.append(cur_n)
            cur_x += self.dt
        return max(n)


a = Settings_sin()
a_n = a.def_n()
b = Settings_sin(10, 11)
b_n = b.def_n()
print(f"sin: [0;1] - {a_n}, [10;11] - {b_n}")



