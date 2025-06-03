brank = '.'
while 1:
	H, W = map(int, raw_input().split())
	if H == 0 and W == 0:
		break
	for h in xrange(H):
		if (h == 0) or (h == H - 1):
			print '#' * W
		else:
			print ('#' + brank * (W - 2) + '#')
	print