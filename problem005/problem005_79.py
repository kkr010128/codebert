def gcd(a, b):
	if b == 0: return a
	else: return gcd(b, a % b)

def lcm(a, b):
	return a * b / gcd(a, b)

while True:
	try:
		a, b = map(int, input().split())
		print(int(gcd(a, b)), int(lcm(a, b)))
	except EOFError:
		break