import sys

N, M, K = [int(s) for s in sys.stdin.readline().split()]
n = 0
A = [0]
for s in sys.stdin.readline().split():
    n = n + int(s)
    A.append(n)

n = 0
B = [0]
for s in sys.stdin.readline().split():
    n = n + int(s)
    B.append(n)

ans = 0
for i in range(N + 1):
    if A[i] > K:
        break
    for j in range(M, -1, -1):
        if A[i] + B[j] <= K:
            ans = max(ans, i + j)
            M = j
            break

print(ans)