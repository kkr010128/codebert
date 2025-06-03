n, k = map(int, input().split())
p = list(map(int, input().split()))
s = sum(p[:k])
ret = s
for i in range(k, n):
    s += p[i] - p[i - k]
    ret = max(ret, s)
print((ret + k) / 2.0)
