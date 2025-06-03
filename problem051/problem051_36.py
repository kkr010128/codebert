def draw(h,w):
	t = "#." * (w/2)
	if w%2 == 0:
		s = t
		k = t.strip("#") + "#"
	else:
		s = t + "#"
		k = "." + t

	for i in range(0,h/2):
		print s
		print k
	if h%2==1:
		print s
	print

if __name__ == "__main__":
	while True:
		h,w = map(int, raw_input().split())
		if h==0 and w==0:
			break
		else:
			draw(h,w)