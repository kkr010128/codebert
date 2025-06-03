while True :
	h,w = map(int,raw_input().split())
	if h==0 and w==0:
		break
	else :
		for i in range(h):
			print '#'*w
		print''