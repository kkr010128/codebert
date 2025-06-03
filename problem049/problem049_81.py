while 1:
	H, W = map(int, input().split())
	if (H == 0 and W == 0) : break
	for i in range(H):
		x = ""
		for j in range(W):
			x += "#"
		print(x)
	print("")