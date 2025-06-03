n, dr = list(map(int, input().split()))
if n >= 10:
	print(dr)
else:
	print(dr+(100*(10-n)))