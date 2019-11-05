from math import *

bot = 0
top = 3
step = 0.00001

def function(x):
	return sin(100*x) * exp(x**2) * cos(2*x)

def Integrate_elementary_segment(x):
	func_k0 = function(x)
	func_k1 = function(x + step / 2)
	func_k2 = function(x + step)
	sum_f = func_k0 + 4 * func_k1 + func_k2
	return step * sum_f / 6

def Integral():
	current_x = bot
	integral = 0
	while (current_x < top):
		integral += Integrate_elementary_segment(current_x)
		current_x += step
	print(integral)

Integral()
