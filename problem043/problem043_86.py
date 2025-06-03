while 1:
	a, b = [int(x) for x in input().split()]
	if a == 0 and b == 0:
		break
	if a > b:
		a, b = b, a
	print(a, b)