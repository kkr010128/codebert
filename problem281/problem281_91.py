import math

I=list(map(int,input().split()))
X=(2*I[1]-I[0])//3
Y=(2*I[0]-I[1])//3
n=X+Y
r=X

if (X<0 or Y<0 or (I[0]+I[1])%3!=0):
    print(0)
    exit()

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
N = 10 ** 6
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

print(cmb(n, r, p))