a = [int(i) for i in input().split()]
if(max(a) > 9):
	print("-1")
else:
	print(a[0] * a[1])