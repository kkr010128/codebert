mod = 10**9+7

def factorials(n,m):
    # 0~n!のリスト
    f = [1,1]
    for i in range(2,n+1):
        f.append(f[-1]*i%m)

    # 0~n!の逆元のリスト
    g = [1]
    for i in range(n):
        g.append(pow(f[i+1],m-2,m))

    return f,g

f,g = factorials(4*10**5,mod)


n,k = map(int, input().split())
if k>=n-1:
    print((f[2*n-1]*g[n]*g[n-1])%mod)
else:
    ans = 0
    for x in range(k+1):
        ans += f[n-1]*g[x]*g[n-x-1]*f[n]*g[n-x]*g[x]
        ans %= mod
    print(ans)