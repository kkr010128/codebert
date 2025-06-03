n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * (n + 1)
for i in range(1, n + 1):
    b[i] = b[i - 1] + a[i - 1]
for i in range(n + 1):
    b[i] -= i
    b[i] %= k
d = dict()
for i in range(min(n + 1, k)):
    if b[i] in d:
        d[b[i]] += 1
    else:
        d[b[i]] = 1
ans = []
j = min(n + 1, k)
for i in range(n):
    ans.append(d[b[i]])
    d[b[i]] -= 1
    if j <= n:
        if b[j] in d:
            d[b[j]] += 1
        else:
            d[b[j]] = 1
    j += 1
ans = sum(ans) - n
print(ans)