import math

top = 10
bot = -10
step = 1
eps = 0.00001

rootlist = list()

def function(x):
	term_1 =  1 / (math.exp(x) * (math.sin(x) + math.cos(x)))
	term_2 = x - math.sin(x) / (math.sin(x) + math.cos(x))
	return term_1 + term_2

def iterator(cur_pos):
	prev_pos = cur_pos
	cur_pos = function(cur_pos)
	while abs(cur_pos - prev_pos) > eps and cur_pos <= top and cur_pos >= bot:
		prev_pos = cur_pos
		cur_pos = function(cur_pos)
	else:
		if cur_pos >= top or cur_pos <= bot:
			return None
	return cur_pos

def solver():
	initial_approximation = bot
	while initial_approximation < top:
		current = initial_approximation
		initial_approximation += step
		temp = iterator(current)
		if temp == None:
			continue
		if temp not in rootlist:
			rootlist.append(temp)


def observelist():
	for first, second in zip(rootlist, rootlist[1:]):
		if abs(first - second) < eps:
			rootlist.remove(first)
	

def run():
	solver()
	observelist()
	print(rootlist)

run()

