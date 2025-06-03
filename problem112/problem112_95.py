n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10**9 + 7
ans = 1

if k == n:
    for i in range(n):
        ans *= a[i]
        ans %= mod
    print(ans)
    exit()
if max(a) < 0 and k%2 == 1:
    a.sort(reverse=True)
    for i in range(k):
        ans *= a[i]
        ans %= mod
    print(ans)
    exit()

a.sort(key=lambda x: abs(x))
cnt = 0
for i in range(1, k+1):
    ans *= a[-i]
    ans %= mod
    if a[-i] < 0:
        cnt += 1

if cnt%2 == 0:
    print(ans)
else:
    a_plus = None
    a_minus = None
    b_plus = None
    b_minus = None
    for i in range(k, 0, -1):
        if a[-i] >= 0 and a_plus == None:
            a_plus = a[-i]
        if a[-i] < 0 and a_minus == None:
            a_minus = a[-i]
    for i in range(k+1, n+1):
        if a[-i] >= 0 and b_plus == None:
            b_plus = a[-i]
        if a[-i] < 0 and b_minus == None:
            b_minus = a[-i]
    if a_plus == None or b_minus == None:
        ans *= pow(a_minus, mod-2, mod)
        ans %= mod
        ans *= b_plus
        ans %= mod
    elif a_minus == None or b_plus == None:
        ans *= pow(a_plus, mod-2, mod)
        ans %= mod
        ans *= b_minus
        ans %= mod
    else:
        if abs(a_plus*b_plus) > abs(a_minus*b_minus):
            ans *= pow(a_minus, mod-2, mod)
            ans %= mod
            ans *= b_plus
            ans %= mod
        else:
            ans *= pow(a_plus, mod-2, mod)
            ans %= mod
            ans *= b_minus
            ans %= mod
    print(ans)