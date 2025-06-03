while True:
	H,W = map(int, raw_input().split(" "))
	if H == 0 and W == 0:
		break
	else:
		for h in xrange(H):
			print "#" * W
		print ""