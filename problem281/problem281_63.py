def cmb(n, k, mod, fac, ifac):
    """
    nCkを計算する
    """
    k = min(k, n-k)
    return fac[n] * ifac[k] * ifac[n-k] % mod


def make_tables(mod, n):
    """
    階乗テーブル、逆元の階乗テーブルを作成する
    """
    fac = [1, 1] 
    ifac = [1, 1] #逆元の階乗テーブル・・・(2)
    inverse = [0, 1] #逆元テーブル・・・(3)

    for i in range(2, n+1):
        fac.append((fac[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod//i)) % mod)
        ifac.append((ifac[-1] * inverse[-1]) % mod)
    return fac, ifac

X,Y=map(int,input().split())

wa = X+Y
if (wa)%3!=0 or not (wa//3 <= X <= wa-wa//3):
    print(0)
else:
    MOD = 10**9 + 7
    fac, ifac = make_tables(MOD, wa // 3)
    ans = cmb(wa // 3, X - wa // 3, MOD, fac, ifac)
    print(ans)
