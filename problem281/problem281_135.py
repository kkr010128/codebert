X, Y = map(int, input().split())

if (2*X-Y)%3==0 and (2*Y-X)%3==0:
    a = (2*X-Y)//3
    b = (2*Y-X)//3
    if a>=0 and b>=0:
        MOD = 10**9+7
        n = a+b+1
        fac = [1]*(n+1)
        rev = [1]*(n+1)
        
        for i in range(1,n+1):
            fac[i] = i*fac[i-1]%MOD
            rev[i] = pow(fac[i], MOD-2, MOD)
        comb = lambda a,b:(fac[a]*rev[a-b]*rev[b])%MOD
        print(comb(a+b, a))
    else:
        print(0)
else:
    print(0)
