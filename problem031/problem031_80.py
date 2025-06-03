while True:
	n = input()
	if n == 0:
		break
	s = map(float, raw_input().split())
	v = sum(map(lambda x: x**2, s)) / n - (sum(s) / n)**2
	print v**0.5