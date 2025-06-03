while True:
	H,W=[int(i) for i in input().split(" ")]
	if H==W==0:
		break

	for h in range(H):
		s="#" if h%2==0 else "."
		for w in range(W-1):
			s+="#" if s[-1]=="." else "." 	
		print(s)
	print()