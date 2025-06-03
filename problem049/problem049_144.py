def draw(h,w):
	s = "#" * w
	for i in range(0,h):
		print s
	print

if __name__ == "__main__":
	while True:
		h,w = map(int, raw_input().split())
		if h==0 and w==0:
			break
		else:
			draw(h,w)