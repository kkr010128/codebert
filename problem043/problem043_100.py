while True :
	a = raw_input().split()
	x = int(a[0])
	y = int(a[1])
	if x == 0 and y == 0 :
		break
	elif x < y :
		print u"%d %d" % (x, y)
	else :
		print u"%d %d" % (y, x)