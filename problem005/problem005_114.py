import sys

def gcd(a,b):
	while a%b :
		a,b=b,a%b
	return b
	
def lcm(a,b) :
	return a*b/gcd(a,b)
	
for ab in sys.stdin:
	a,b = map(int,ab.split())
	a,b = max(a,b),min(a,b)
	print "%d" % gcd(a,b),
	print "%d" % lcm(a,b)