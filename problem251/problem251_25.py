N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())

import numpy as np

#0: g, R
#1: c, S
#2: p, P

ans = 0
L = [[] for _ in range(K)]
for i in range(K):
    L[i] = T[i:N:K]
for l in L:
#    print()
#    print(l)
    lenl = len(l)
    Dp = np.zeros([lenl+1, 3], dtype=int)
    Dp[:][:] = -1
    Dp[0][:] = 0
#    print(Dp)
    ll = l[0]
    if ll == 'r':
        Dp[1][0] = 0
        Dp[1][1] = 0
        Dp[1][2] = P
    elif ll == 's':
        Dp[1][0] = R
        Dp[1][1] = 0
        Dp[1][2] = 0
    elif ll == 'p':
        Dp[1][0] = 0
        Dp[1][1] = S
        Dp[1][2] = 0

    for i in range(1, lenl):
        ll = l[i]
        if ll == 'r':
            Dp[i+1][0] = max(Dp[i][1], Dp[i][2])
            Dp[i+1][1] = max(Dp[i][2], Dp[i][0])
            Dp[i+1][2] = max(Dp[i][0], Dp[i][1]) + P
        elif ll == 's':
            Dp[i+1][0] = max(Dp[i][1], Dp[i][2]) + R
            Dp[i+1][1] = max(Dp[i][2], Dp[i][0])
            Dp[i+1][2] = max(Dp[i][0], Dp[i][1])
        elif ll == 'p':
            Dp[i+1][0] = max(Dp[i][1], Dp[i][2])
            Dp[i+1][1] = max(Dp[i][2], Dp[i][0]) + S
            Dp[i+1][2] = max(Dp[i][0], Dp[i][1])
#    print(Dp)
    ans += max(Dp[-1][:])
print(ans)