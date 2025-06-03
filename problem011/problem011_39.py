a, b = map(int, raw_input().split())

def gcd(a,b):
	c = a%b
	if c==0:
		return b
	elif c == 1:
		return c
	else:
		return gcd(b, c)

if a > b:
	print gcd(a, b)
elif a < b:
	print gcd(b, a)
else:
	print a