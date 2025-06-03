import sys
def gcd(a,b):
	if b != 0:
		return gcd(b,a%b)
	else:
		return a
def lcm(a,b,g):
	return b / g * a
for s in sys.stdin:
	ls = map(int,s.split(' '))
	print "%d %d" % (gcd(ls[0],ls[1]),lcm(ls[0],ls[1],gcd(ls[0],ls[1])))