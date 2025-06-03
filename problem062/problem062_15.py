a = raw_input()
while a!='0':
	s = 0
	for i in range(len(a)):
		s += int(a[i])

	print s
	a = raw_input()