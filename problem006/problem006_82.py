def debt(x):
	nx = x * 105 / 100
	ha = nx % 1000
	nx -= ha
	if ha != 0:
		nx += 1000
	
	return nx

n = int(raw_input())
x = 100000

for i in range(0, n):
	x = debt(x)

print x