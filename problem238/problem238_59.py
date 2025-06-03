n, k, s = map(int, input().split())

A = [0] * n

if s == 10 ** 9:
	for i in range(k):
		A[i] = 10 ** 9
	for i in range(k, n):
		A[i] = 1

else:
	for i in range(k):
		A[i] = s
	for i in range(k, n):
		A[i] = s + 1

print(*A)