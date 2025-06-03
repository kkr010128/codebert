def gcd(a, b):
	if a < b:
		tmp = a
		a = b
		b = tmp
	
	r = a % b
	while r != 0:
		a = b
		b = r
		r = a % b

	return b

if __name__ == '__main__':
	l = list(map(int, input().split()))
	x = l[0]
	y = l[1]

	ans = gcd(x, y)
	print(ans)