while 1:
	x, y = map(int, raw_input().split())
	if x == y == 0:
		break
	else:
		if x < y:
			print "%d %d" % (x, y)
		else:
			print "%d %d" % (y, x)