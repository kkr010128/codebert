import warnings


n = 0
i = 0
while (n == 0): 

	i = i + 1

	data = map(int, raw_input().split())
	x = data[0]
	y = data[1]

	if(x == 0 and y == 0):
		break
	else:
		if x > y:
			print "%s %s" % (y, x)
		else:
			print "%s %s" % (x, y)