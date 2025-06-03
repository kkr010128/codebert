# coding: utf-8

while True:
	try:
		data = map(int, raw_input().split())
		if data[0] > data[1]:
			a = data[0]
			b = data[1]
		else:
			a = data[1]
			b = data[0]
		
		r = 1
		while r > 0:
			q = a / b
			r = a - b * q
			a = b
			b = r
		gcd = a
		lcm = data[0] * data[1] / gcd

		print("{:} {:}".format(gcd, lcm))

	except EOFError:
		break