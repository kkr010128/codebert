n, k = map(int, input().split())
p = list(map(int, input().split()))
for i in range(n):
    p[i] = (p[i] + 1) / 2
ans = sum(p[:k])
pre = sum(p[:k])
for j in range(k, n):
    pre = pre + p[j]- p[j - k]
    ans = max(ans, pre)
print(ans)