N = int(input())
A = [0] * (N + 1)
B = [0] * (N + 1)

count = 0

for i in range(1, N + 1):
  A[i], B[i] = map(int, input().split())

A.sort()
B.sort()
if N % 2 == 1:
  centerA = A[(N + 1) // 2]
  centerB = B[(N + 1) // 2]
else:
  centerA = (A[N // 2] + A[N // 2 + 1]) / 2
  centerB = (B[N // 2] + B[N // 2 + 1]) / 2

#print(centerA, centerB)  

if N % 2 == 1:
  count = centerB - centerA + 1
else:
  count = (centerB - centerA) * 2 + 1

print(int(count))