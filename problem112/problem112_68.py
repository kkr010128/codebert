n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 1
mod = 10**9 + 7
c = 0
z = 0
for i in a:
    if i < 0:
        c += 1
    elif i == 0:
        z += 1
if c == n and k & 1:
    a.reverse()
    for i in range(k):
        ans *= -a[i]
        ans %= mod
    print(-ans % mod)
elif c == n:
    for i in range(k):
        ans *= -a[i]
        ans %= mod
    print(ans)
elif k == n:
    for i in a:
        ans *= abs(i)
        ans %= mod
    print(((-1)**(c & 1) * ans) % mod)
else:
    plus = [i for i in a if i > 0]
    minus = [i for i in a if i <= 0]
    plus.sort(reverse=1)
    minus.sort()
    plus += [0] * z
    x = len(plus)
    y = len(minus)
    p, m = 0, 0
    if k & 1:
        ans *= plus[0]
        p += 1
    for i in range(k // 2):
        if x - 1 <= p:
            ans *= minus[m] * minus[m + 1]
            m += 2
        elif y - 1 <= m:
            ans *= plus[p] * plus[p + 1]
            p += 2
        else:
            if minus[m] * minus[m + 1] >= plus[p] * plus[p + 1]:
                ans *= minus[m] * minus[m + 1]
                m += 2
            else:
                ans *= plus[p] * plus[p + 1]
                p += 2
        ans %= mod

    print(ans % mod)
