n, k = map(int, input().split())
p = list(map(lambda x: (1+int(x))/2, input().split()))
s = sum(p[0:k])
ans = s
for i in range(k, n):
    s += p[i] - p[i-k]
    ans = max(ans, s)
print(ans)