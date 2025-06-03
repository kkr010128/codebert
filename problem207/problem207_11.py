A = [[j for j in list(map(int, input().split()))] for i in range(3)]
N = int(input())
B = []
for _ in range(N):
	b = int(input())
	for r in A:
		for i in range(len(r)):
			if r[i] == b:
				r[i] = 0
ans = False
for i in range(3):
	if sum(A[i]) == 0:
		ans = True
if not ans:
	for i in range(3):
		if A[0][i] + A[1][i] + A[2][i] == 0:
			ans = True
if not ans:
	if A[0][0] + A[1][1] + A[2][2] == 0:
		ans = True
	elif A[0][2] + A[1][1] + A[2][0] == 0:
		ans = True
if ans:
	print('Yes')
else:
	print('No')
