import sys

def lcm(a,b):
	return a*b//gcd(a,b)

def gcd(a,b):
	while True:
		a,b = b,a%b
		if b==0:
			return a

for line in sys.stdin:
	a,b = map(int, line.split())
	print("{} {}".format(gcd(a,b),lcm(a,b)))