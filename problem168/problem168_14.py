N,M = list(map(int,input().split()))
A = list(map(int,input().split()))

sum = 0
for i in range(M):
	sum = sum + A[i]

if N > sum:
	print(N - sum)
elif N == sum:
	print(0)
else:
	print(-1)