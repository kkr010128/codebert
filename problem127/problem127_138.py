X, Y = map(int, input().split())
Z = X * 4 - Y

if Z % 2 == 0 and X * 2 >= Z >= 0:
	print('Yes')
else:
	print('No')