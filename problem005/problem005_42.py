def gcd(a,b):
	while a>0 and b>0:
		if a<b:
			b -= a
		elif a>b:
			a -= b
		else:
			return a
	raise

def lcm(a,b):
	return a*b/gcd(a,b)


while True:
	try:
		inp = raw_input()
	except EOFError:
		break
	a, b = map((lambda x: int(x) ), inp.split())

	print gcd(a,b),lcm(a,b)