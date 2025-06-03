import bisect
n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a2 = [0] * (n + 1)
b2 = [0] * (m + 1)
for i in range(0, n):
    a2[i+1] = a[i] + a2[i]
for i in range(0, m):
    b2[i+1] = b[i] + b2[i]

ans = 0
for i in range(n+1):
    tmp = bisect.bisect_right(b2, k-a2[i]) - 1
    if a2[i] + b2[tmp] <= k and tmp >= 0:
        ans = max(ans, i+tmp)

print(ans)