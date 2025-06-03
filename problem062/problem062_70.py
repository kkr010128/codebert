while True:
	a = input()
	if a == "0":
		break
	print(sum([int(a[i]) for i in range(len(a))]))