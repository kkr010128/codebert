def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a%b)
while True:
	try:
		a, b = map(int, raw_input().strip().split(' '))
		print "%d %d" % (gcd(a, b), a*b/gcd(a, b))
	except EOFError:
		break