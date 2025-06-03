H,N = map(int,input().split())
AB = [tuple(map(int,input().split())) for _ in range(N)]
INF = float("inf")
dp0 = [INF]*(H+1)
dp1 = [0]*(H+1)
dp0[0] = 0
for i in range(N):
    a,b = AB[i]
    dp1[H] = dp0[H]
    for h in range(H-1, -1, -1):
        dp1[h] = min(dp0[h], dp1[h+1])
    for h in range(H+1):
        dp1[h] = min(dp1[h], dp1[max(h-a,0)]+b)
    t = dp1
    dp1 = dp0
    dp0 = t
print(dp0[H])