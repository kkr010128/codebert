def prod(list):
    prod = 1
    for k in list:
        prod = (prod * k) % (10**9+7)
    return prod
    
    


n, kk = map(int, input().split())
a = list(map(int, input().split()))

plus = []
minus = []

for k in a:
    if k >= 0:
        plus.append(k)
    if k <= 0:
        minus.append(k)

if len(plus) == 0:
    if kk % 2 == 0:
        mi = sorted(minus)
        ans = prod(mi[:kk])
    else:
        mi = sorted(minus, reverse=True)
        ans = prod(mi[:kk])

    print(int(ans) % (10**9+7))

elif n == kk:
    ans = prod(a)
    print(int(ans) % (10**9+7))

else:
    mi = sorted(minus)
    pl = sorted(plus, reverse=True)
    mi.append(0)
    mi.append(0)
    pl.append(0)
    pl.append(0)
    miind = 0
    plind = 0
    ans = 1
    while kk > miind + plind:
        if mi[miind]*mi[miind+1] > pl[plind]*pl[plind+1] and kk != miind + plind + 1:
            ans = (ans*mi[miind]*mi[miind+1]) % (10**9+7)
            miind += 2
        else:
            ans = (ans*pl[plind]) % (10**9+7)
            plind += 1

    print(ans)