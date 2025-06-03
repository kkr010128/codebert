n,k,s = map(int,input().split())
INF = 10**9

ans = [INF] * n

if s == INF:
    ans = [1] * n

for i in range(k):
    ans[i] = s
    
print(*ans)