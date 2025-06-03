n = int(input())
a = list(map(int, input().split()))

ret = 0
now = a[0]
for i in range(1, n):
    if now > a[i]:
        ret += now - a[i]
        a[i] = now
    now = a[i]

print(ret)