A, B, C = list(map(int, input().split()))
s = set([A, B, C])
if len(s) == 1 or len(s) == 3:
	print('No')
else:
	print('Yes')
