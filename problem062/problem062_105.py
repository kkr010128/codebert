while 1:
	x = raw_input()
	if x == '0':
		break
	s = 0
	for i in xrange(len(x)):
		s += int(x[i])
	print s