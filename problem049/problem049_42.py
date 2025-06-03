while True:
	h,w = [int(s) for s in input().split(' ')]
	if h==0 and w==0:
		break
	else:
		low = '#' * w
		rectangle = (low+'\n') * h
		print(rectangle)