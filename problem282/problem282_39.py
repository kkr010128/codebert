import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, T = mapint()
AB = [list(mapint()) for _ in range(N)]
AB.sort()
maxtime = AB[-1][0]
Bs = [b for a, b in AB]
dp = [0]*(T)

ans = 0
for n in range(N-1):
    a, b = AB[n]
    newdp = [0]*(T)
    for i in range(T):
        if a<=i and i-a<T:
            newdp[i] = max(dp[i], dp[i-a]+b)
    dp = newdp
    ans = max(ans, max(dp)+max(Bs[n+1:]))

print(ans)