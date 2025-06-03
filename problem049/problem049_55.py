while 1:
	H, W = map(int, raw_input().split())
	if H == W == 0:
		break
	for i in range(H):
		print "#" * W
	print ""