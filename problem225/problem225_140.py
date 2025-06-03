H, A = (int(x) for x in input().split())
dm = divmod(H,A)
if dm[1] == 0:
	print(dm[0])
else:
	print(dm[0]+1)