H, N = list(map(int, input().split()))
A = list(map(int, input().split()))

AS = sum(A)
if AS >= H:
	print('Yes')
else:
	print('No')
