S = int(input())
p = 10**9 +7

def pow_mod(p,a,n):
    res = 1
    while n > 0:
        if n % 2 == 1:
            res = (res * a) % p
        n = n // 2
        a = (a*a)%p
    return res

n = 2000
fac = [1]
foo = 1
for i in range(1,n+1):
    foo = (foo*i)%p
    fac.append(foo)

#コンビネーションのmod
def comb_mod(n,k):
    res = (fac[n] * pow_mod(p,fac[k],p-2) * pow_mod(p,fac[n-k],p-2)) % p
    return res

ans = 0
for i in range(1,1+S//3):
    t = S - 3*i
    ans = (ans + comb_mod(t+i-1,t)) %p

print(ans)