import sys
n, k = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))
a.sort()
f.sort(reverse=True)
l, r = -1, 10 ** 12 + 1
while r - l > 1:
    m = (l + r) // 2
    cnt = 0
    for i in range(n):
        cnt += max(0, a[i] - (m // f[i]))
    if cnt <= k:
        r = m
    else:
        l = m
print(r)