while 1:
	s,t = map(int,input().split())
	if s>t:
		s,t = t,s
	if (s,t)==(0,0):
		break
	print(s,t)