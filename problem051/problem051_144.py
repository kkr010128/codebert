while True:	
	H,W = map(int, input().split())
	if H==0 and W==0: break
	for y in range(0,H):
		for x in range(0,W):
			if y%2==1:
				if x%2==1: print("#",end="")
				else: print(".",end="")
			else:
				if x%2==1: print(".",end="")
				else: print("#",end="")
		print()
	print()
