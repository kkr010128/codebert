def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

from math import gcd

mod = int(1e9+7)
n = ii()
cnd = {}
azero = 0
bzero = 0
allzero = 0
for _ in range(n):
    a,b = iim()
    if a*b == 0:
        if a == 0 and b != 0:
            azero += 1
        elif a != 0 and b == 0:
            bzero += 1
        else:
            allzero += 1
    else:
        g = gcd(a,b)
        a //= g
        b //= g
        if a<0:
            a *= -1
            b *= -1
        before = cnd.get((a,b),False)
        if b > 0:
            check = cnd.get((b,-a),False)
        else:
            check = cnd.get((-b,a),False)
        if before:
            cnd[(a,b)] = [before[0]+1,before[1]]
        elif check:
            if b > 0:
                cnd[(b,-a)] = [check[0],check[1]+1]
            else:
                cnd[(-b,a)] = [check[0],check[1]+1]
        else:
            cnd[(a,b)] = [1,0]

cnd[0] = [azero,bzero]
noreg = 0
ans = 1
#print(cnd)
for item in cnd.values():
    if item[0] == 0  or item[1] == 0:
        noreg += max(item[0],item[1])
    else:
        ans *= (2**item[0]+2**item[1]-1)
        ans %= mod
print((ans*((2**noreg)%mod)-1+allzero)%mod)