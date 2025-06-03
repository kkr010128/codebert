while 1:
	a,b = map(int, raw_input().split())
	if a == b == 0:
		break
	elif a < b:
		print "%s %s" % (a,b)
	else:
		print "%s %s" % (b,a)