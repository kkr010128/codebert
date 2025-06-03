while 1:
	x = list(raw_input())
	if int(x[0]) == 0:
		break
	sum = 0
	for n in x:
		sum += int(n)
	print sum