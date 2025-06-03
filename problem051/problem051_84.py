while True:
	H,W = map(int, raw_input().split(" "))
	if H == 0 and W == 0:
		break
	else:
		for h in xrange(H):
			sw = True if (h % 2) == 0 else False
			s = ""
			for w in xrange(W):
				s += "#" if sw else "."
				sw = not sw
			print s
		print ""