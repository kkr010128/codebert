while True:
	s = raw_input()
	if s == '0':
		break
	n = 0
	for i in s:
		n += int(i)
	print n