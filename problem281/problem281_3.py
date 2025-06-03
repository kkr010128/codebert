
[X,Y] = list(map(int,input().split()))

n = (-1*X+2*Y)//3
m = (2*X-Y)//3

if (X+Y)%3 !=0:
    print(0)

elif n<0 or m<0:
    print(0)

else:
    MAXN = (10**6)+10
    MOD = 10**9 + 7
    f = [1]
    for i in range(MAXN):
        f.append(f[-1] * (i+1) % MOD)
    def nCr(n, r, mod=MOD):
        return f[n] * pow(f[r], mod-2, mod) * pow(f[n-r], mod-2, mod) % mod


    print(nCr(n+m,n,10**9 + 7))
