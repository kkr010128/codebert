N ,K = map(int,input().split())
Ps = list(map(int,input().split()))

Ps.sort()
ans = 0
for i in range(K):
    ans += Ps[i]
print(ans)
