def draw_frame(h, w):
	print("#" * w)
	print(("#" + "." * (w - 2) + "#\n") * (h - 2), end="")
	print("#" * w + "\n")

while True:
	H, W = map(int, input().split())
	if H == W == 0: break
	draw_frame(H, W)