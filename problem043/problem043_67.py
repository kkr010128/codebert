while True:
	a = map(int, raw_input().split(" "))
	if len([x for x in a if x <> 0]) <= 0:
		break
	else:
		a.sort()
		print " ".join(map(str, a))