first_flag = True

while True:
	H, W = map(int, input().split())
	if H == 0 and W == 0: break
	if not first_flag:
		print()
		first_flag = False
	print(("#" * W + "\n") * H)