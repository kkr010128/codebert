x, k, d = map(int, input().split())

x = abs(x)
kk = x // d
amari = x % d

if kk >= k:
    ans = (kk - k) * d + amari
elif (k - kk) % 2 == 1:
    ans = abs(amari - d)
else:
    ans = amari

print(ans)