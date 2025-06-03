n = int(input())
A = list(map(int, input().split()))
for i in range(n - 1):
	A[i + 1] += A[i]
minv = float('inf')
for a in A[:-1]:
	minv = min(minv, abs(A[-1]/2 - a))
print(int(minv * 2))