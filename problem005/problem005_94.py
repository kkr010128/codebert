import sys

def euclid(x, y):
	if y == 0: return x
	elif x < y: return euclid(y, x)
	else: return euclid(y, x%y)

for line in sys.stdin:
	a, b = map(int, line.split())
	gcd = euclid(a, b)
	lcm = a*b/gcd
	print str(gcd)+' '+str(lcm)
