while True:
	H,W = list(map(int, input().split()))
	if (H == 0 and W == 0):
		break
	else:
		for n in range(H):
			s = ""
			for m in range(W):
				if (0 < n and n < H-1) and (0 < m and m < W-1):
					s += "."
				else:
					s += "#"
			print(s)
		print("")