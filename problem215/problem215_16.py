n,K = map(int, input().split())
mod = 10**9 + 7

def modcomb(n,a,mod):
    cnt = 1
    for i in range(a):
        cnt *= (n-i)
        cnt *= pow(i+1,mod-2,mod)
        cnt %= mod
    # print(cnt)
    return cnt

def modconb(n,mod):
    # テーブルを作る
    fac = [0]*(n+1)
    finv = [0]*(n+1)
    inv = [0]*(n+1)  

    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2,n+1):
        fac[i] = fac[i-1]*i % mod
        inv[i] = mod - inv[mod%i] * (mod//i) % mod
        finv[i] = finv[i-1] * inv[i] %mod
    return fac,finv
    # return(fac[n]*(finv[k]*finv[n-k]%mod)%mod)


cnt = 0
if n-1 >= K:
    fac1,finv1 = modconb(n,mod)
    for k in range(K+1):
        c1 = fac1[n]*(finv1[k]*finv1[n-k]%mod)%mod
        c2 = fac1[n-1]*(finv1[k]*finv1[n-1-k]%mod)%mod
        cnt += c1*c2
        cnt %= mod
    print(cnt%mod)
else:
    cnt1 = modcomb(2*(n-1),n-1,mod)
    cnt2 = modcomb(2*(n-1),n,mod)
    ans = (cnt1+cnt2)%mod
    print(ans)