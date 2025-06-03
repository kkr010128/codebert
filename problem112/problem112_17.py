n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

plus = []
minus = []
for i in a:
    if i > 0: plus.append(i)
    if i < 0: minus.append(i)

ans = 1
if k > len(plus) + len(minus):
    ans = 0
elif len(minus) == 0:
    plus.sort(reverse=True)
    for i in range(k):
        ans = (ans * plus[i]) % mod
elif len(plus) == 0:
    if k % 2 == 0:
        minus.sort()
        for i in range(k):
            ans = (ans * minus[i]) % mod
    else:
        if n != len(minus):
            ans = 0
        else:
            minus.sort(reverse=True)
            for i in range(k):
                ans = (ans * minus[i]) % mod
elif k == len(plus) + len(minus) and (len(minus) % 2) == 1:
    if n != len(plus) + len(minus):
        ans = 0
    else:
        for x in plus:
            ans = (ans * x) % mod
        for y in minus:
            ans = (ans * y) % mod
else:
    plus.sort(reverse=True)
    minus.sort()
    i, j = 0, 0
    if k % 2 == 1:
        ans = plus[0]
        i = 1
    while i + j < k:
        tmp_p = plus[i] * plus[i + 1] if i <= len(plus) - 2 else 1
        tmp_m = minus[j] * minus[j + 1] if j <= len(minus) - 2 else 1
        if tmp_p >= tmp_m:
            ans = (ans * (tmp_p % mod)) % mod
            i += 2
        else:
            ans = (ans * (tmp_m % mod)) % mod
            j += 2
print(ans)
