n,k = map(int,input().split())
mod = 10**9+7
ans = 0

kosu = [0 for i in range(k+1)]

for i in range(k, 0, -1):
    kin = 1  ## kosuに入れる数
    nn = k//i    ## iの倍数が何個あるかを計算する
    ii = n
    kini = nn
    while ii > 0:
        if ii%2 == 1:
            kin = (kin*kini)%mod
        kini = (kini**2)%mod
        ii //= 2
    for j in range(2,nn+1):
        kin = (kin-kosu[j*i])%mod
    kosu[i] = kin

for i in range(1,k+1):
    ans = (ans+(kosu[i]*i)%mod)%mod

print(ans)
