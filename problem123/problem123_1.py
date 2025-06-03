N = int(input())
A = list(map(int, input().split()))

XOR = 0

for i in range (0, N):
	XOR= XOR^A[i]

B = []

for i in range (0, N):
	B.append(XOR^A[i])

print(*B)