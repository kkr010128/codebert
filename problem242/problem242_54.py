#n<=10**5まで
def cmb(n, k, mod, fac, ifac):    
    k = min(k, n-k)
    return fac[n] * ifac[k] * ifac[n-k] % mod


def make_tables(mod, n):
    fac = [1, 1] # 階乗テーブル・・・(1)
    ifac = [1, 1] #逆元の階乗テーブル・・・(2)
    inverse = [0, 1] #逆元テーブル・・・(3)

    for i in range(2, n+1):
        fac.append((fac[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod//i)) % mod)
        ifac.append((ifac[-1] * inverse[-1]) % mod)
    return fac, ifac



n,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
mod = 1000000007
fac, ifac = make_tables(mod, n)


ans = 0
for i in range(n-k+1):
    c = cmb(n-1-i, k-1, mod, fac, ifac)
    ans += ((a[n-1-i] - a[i]) * c) % mod
print(ans%mod)