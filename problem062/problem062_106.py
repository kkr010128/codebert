while 1:
	a = raw_input()
	if a =='0':
		break
	sum = 0
	for i in a:
		sum += int(i)
	print sum