def draw(h,w):
	s = "#" * w
	k = "#" + "." * (w-2) + "#"
	print s
	for i in range(0,h-2):
		print k
	print s
	print

if __name__ == "__main__":
	while True:
		h,w = map(int, raw_input().split())
		if h==0 and w==0:
			break
		else:
			draw(h,w)