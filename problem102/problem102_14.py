import math

N, K = map(int,input().split())
A = list(map(int,input().split()))
B = [0] * (N + 1)
M = [0] * (N + 1)

for i in range(N):
    B[i + 1] = B[i] + math.log10(A[i])

for i in range(K, N + 1):
    M[i] = B[i] - B[i - K]

for i in range(K + 1, N + 1):
    if M[i - 1] + 1e-10 < M[i]:
        print("Yes")
    else:
        print("No")