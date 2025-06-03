N = int(input())
A = []
B = []
for i in range(N):
	a, b = map(int, input().split())
	A.append(a)
	B.append(b)

A.sort()
B.sort()

if N % 2 == 1:
	A_median = A[N // 2]
	B_median = B[N // 2]
	print(B_median - A_median + 1)
else:
	A_median2 = A[(N - 1) // 2] + A[N // 2]
	B_median2 = B[(N - 1) // 2] + B[N // 2]
	print(B_median2 - A_median2 + 1)