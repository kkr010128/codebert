if __name__ == "__main__":
	W, H, x, y, r = input().split()
	W, H, x, y, r = int(W), int(H), int(x), int(y), int(r)
	
	if (x - r) < 0 or W < (x + r) or (y - r) < 0 or H < (y + r):
		print("No")
	else:
		print("Yes")