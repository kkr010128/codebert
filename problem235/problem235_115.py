N = int(input())
A = list(map(int, input().split()))
from collections import Counter
def factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    c = Counter(fct)
    return c

def solve(N,A):
    ans = 0
    mod = 10**9+7
    fcts = [0]*10**6
    for a in A:
        c = factorize(a)
        for k,v in c.items():
            fcts[k] = max(fcts[k],v)
    prod = 1
    for i,f in enumerate(fcts):
        if f==0:
            continue
        prod *= pow(i,f)
        prod %= mod
    for a in A:
        ans += prod*pow(a,mod-2,mod)
        ans %= mod
    return ans
print(solve(N,A))