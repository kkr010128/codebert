import sys

N, T = map(int, input().split())
S = sys.stdin.readlines()
A = []
B = []
for s in S:
    a, b = map(int, s.split())
    A.append(a)
    B.append(b)

dp1 = [[0] * T for _ in range(N + 1)]
for i in range(N):
    for j in range(T):
        here = dp1[i][j]
        if j < A[i]:
            dp1[i + 1][j] = here
        else:
            dp1[i + 1][j] = max(here, dp1[i][j - A[i]] + B[i])

dp2 = [[0] * T for _ in range(N + 2)]
for i in range(N, 0, -1):
    for j in range(T):
        here = dp2[i + 1][j]
        if j < A[i - 1]:
            dp2[i][j] = here
        else:
            dp2[i][j] = max(here, dp2[i + 1][j - A[i - 1]] + B[i - 1])

ans = 0
for i in range(1, N + 1):
    t = 0
    for j in range(T):
        t2 = dp1[i - 1][j] + dp2[i + 1][T - 1 - j]
        t = max(t, t2)
    ans = max(ans, t + B[i - 1])

print(ans)
