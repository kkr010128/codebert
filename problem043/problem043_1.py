while True:
	t = input().split()
	a = int(t[0])
	b = int(t[1])
	if (a == 0) and (b == 0):
			break
	if (a < b):
		print(str(a) + " " + str(b))
	else:
		print(str(b) + " " + str(a))