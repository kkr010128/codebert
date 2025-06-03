N, K, S = map(int, input().split())
INF = int(1e9)
if S == INF:
    ans = [INF]*K + [INF-1]*(N-K)
else:
    ans = [S]*K + [INF]*(N-K)

for e in ans:
    print(e, end=" ")