import numpy as np
from math import *

def Jacoby(x, y):
	matr = np.array([[2 * x, 2 * y], [-1, 3*(y-1)**2]])
	return np.linalg.inv(matr)

def Free_coef(x, y):
	return np.array([x ** 2 + y ** 2 - 9, (y-1)**3 -x + 1])

def JF(x, y):
	jacoby = Jacoby(x, y)
	free = Free_coef(x, y)
	return np.dot(jacoby, free)

eps = 0.00001

def solver(x, y):
	x0 = np.array([0, 0])
	x1 = np.array([x, y])
	while (np.linalg.norm(x0-x1) > eps):
		x0 = x1
		x1 = x0 - JF(x0[0], x0[1])
	return x1

rootlist = list()

step = 0.1
bot = -3
top = -1.5
current_x = bot

def addinlist(rlist, vect):
	for element in rlist:
		if abs(element[0] - vect[0]) < eps and abs(element[1] == vect[1]) < eps:
			return None
		else:
			continue
	rlist.append(vect)



while (current_x <= top):
	root = solver(current_x, 0)
	addinlist(rootlist, root)
	current_x += step

print(rootlist)




bot = 3/2
top = 5/2
current_x = bot


while (current_x <= top):
	root = solver(current_x, 0)
	addinlist(rootlist, root)
	current_x += step

print(rootlist)
