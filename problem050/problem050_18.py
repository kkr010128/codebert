while True:
	[H, W] = list(map(int, input().split()))

	if H == 0 and W == 0:
		break

	for i in range(H):
		for j in range(W):
			if i > 0 and i < H - 1 and j > 0 and j < W - 1:
				print(".", end = "")
			else:
				print("#", end = "")
		print("")
	print("")