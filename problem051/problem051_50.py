def draw(h, w):
	for i in range(h):
		if i % 2 == 0:
			print(("#."*w)[:w])
		else:
			print((".#"*w)[:w])
	print("")


while True:
	H, W = map(int, input().split())
	if H == W == 0: break
	draw(H, W)