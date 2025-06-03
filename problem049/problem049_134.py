while 1:
	H , W = map(int, raw_input().split())
	if H == 0 and W == 0:
		break
	for l in range(0,H):
		print '#' * W
	print 