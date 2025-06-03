while True:
	(x, y) = map(lambda s:int(s), input().split())
	if x == 0 and y == 0:
		break
	if x > y:
		(x, y) = (y, x)
	print(x, y)