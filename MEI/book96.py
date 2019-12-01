from math import *
 

def decorator_fun(a):
    def fun(x):
        return x+0.5*sin(x)+a
    return fun
 


def solve(a):
    if __name__=='__main__':
        func = decorator_fun(a)
        global e
        a=float(input("x1="))
        b=float(input("x2="))

        x1 = a
        x2 = b
        x = (x2+x1)/2
        res = None
        while abs(x2-x1) >= e:
            x = (x2+x1)/2
            if func(x)*func(x2) > 0:
                x2 = x
            elif func(x)*func(x2) < 0:
                x1 = x
            else:
                break
        
        print('x={}\n'.format(x))


e=float(input("Accuracy e="))
for a in [-1, 1, -2, 2, -3, 3]:
    print("a={}:".format(a))
    solve(a)
                
                
        