def code():
	l = []
	while True:
		m,f,r = map(int,input().split())
		if m == f == r == -1:
			break
		else:
			l.append([m,f,r])
	for i in l:
		s = ''
		x = i[0]+i[1]
		if i[0] == -1 or i[1] == -1:
			s = 'F'
		elif x >= 80:
			s = 'A'
		elif x >= 65:
			s = 'B'
		elif x >= 50:
			s = 'C'
		elif x >= 30:
			s = 'D'
			if i[2] >= 50:
				s = 'C'
		else:
			s = 'F'
		print(s)
code()