n, k = map(int, input().split())
p = list(map(int, input().split()))

e = [(p[i]+1)/2 for i in range(n)]

tmp = sum(e[:k])
ans = tmp
for i in range(n-k):
    tmp += (e[i+k]-e[i])
    ans = max(ans, tmp)

print(ans)