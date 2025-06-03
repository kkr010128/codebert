"""
気付き
１、float('inf')はちょい遅いみたい
２、input()よりもinput = sys.stdin.readlineの方が爆速らしい（知らんがな）
"""
import sys
inf = 10 ** 15
input = sys.stdin.readline

N, M, L = map(int, input().split())
dp = [[inf] * N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    dp[a-1][b-1] = c
    dp[b-1][a-1] = c
for i in range(N):
    dp[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
#print('distance={}'.format(dp))


dp2 = [[inf] * N for _ in range(N)]
for a in range(N - 1):
    for b in range(a+1, N):
        if dp[a][b] <= L:
            dp2[a][b] = 1
            dp2[b][a] = 1
for k in range(N):
    for i in range(N):
        for j in range(N):
            dp2[i][j] = min(dp2[i][j], dp2[i][k] + dp2[k][j])
#print('times={}'.format(dp2))


Q = int(input())
for _ in range(Q):
    s, t = map(int, input().split())
    cost = dp2[s-1][t-1]
    if cost != inf:
        print(cost - 1)
    else:
        print(-1)
