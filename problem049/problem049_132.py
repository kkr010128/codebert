while True:
	a,b=map(int,raw_input().split())
	if a+b==0:
		break
	print ('#'*b+'\n')*a