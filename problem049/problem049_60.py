import warnings
import sys




x = 0
while (x == 0):
	args = map(int, raw_input().split())

	h = args[0]
	w = args[1]

	if (h == 0 and w == 0):
		break

	for i in range(h):
			for j in range(w):
				sys.stdout.write("#")
			print ""
	print ""  