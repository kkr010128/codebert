n, k = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a[:k])
mx = s
for i in range(k, n):
    s += a[i] - a[i - k]
    mx = max(mx, s)
print((mx + k) / 2)