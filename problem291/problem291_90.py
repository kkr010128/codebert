x=list(map(int, input().split()))
if x[1]*2>x[0]:
	print(0)
else:
	print(x[0]-x[1]*2)