def nCr(n,r,mod):
    p=1
    q=1
    
    # print(n,r)

    
    for i in range(r):
        
        q *= i+1
        q %= mod
        
        p *= n-i
        p %= mod

    # print(p,q)
    return (p * pow(q,mod-2,mod)) % mod

s=int(input())
mod = 10**9+7

ans = 0

for i in range(1,s//3+1):
    
    if i==1:
        h=1
        
    else:    
        h=nCr(s-3*i+i-1 ,i-1, mod)
        
    ans += h
    ans %= mod
    # print(h)

print(ans)