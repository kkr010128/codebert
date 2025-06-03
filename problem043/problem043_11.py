while True:
	ia=[int(i) for i in input().split(" ")]
	if ia[0]==ia[1]==0:
		break
	print(" ".join([str(i) for i in sorted(ia)]))