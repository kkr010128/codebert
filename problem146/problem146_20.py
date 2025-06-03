import math


n = int(input())
mod = 1000000007
ab = [list(map(int,input().split())) for _ in range(n)]
dic = {}
z = 0
nz,zn = 0,0
for a,b in ab:
    if a == 0 and b == 0:
        z += 1
        continue
    elif a == 0:
        zn += 1
        continue
    elif b == 0:
        nz += 1
    if a< 0:
        a = -a
        b = -b
    g = math.gcd(a,b)
    tp = (a//g,b//g)
    if tp not in dic:
        dic[tp] = 1
    else:
        dic[tp] += 1
    
ans = 1
nn = n - z - zn - nz
for tp,v in dic.items():
    if v == 0:
        continue
    vt = (tp[1],-1*tp[0])
    if vt in dic:
        w = dic[vt]
        #print(tp)
        e = pow(2,v,mod) + pow(2,w,mod) - 1
        ans *= e
        ans %= mod
        nn -= v + w 
        dic[tp] = 0
        dic[vt] = 0
ans *= pow(2,nn,mod)
if zn == 0:
    ans *= pow(2,nz,mod)
elif nz == 0:
    ans *= pow(2,zn,mod)
else:
    ans *= pow(2,nz,mod) + pow(2,zn,mod) - 1
ans += z - 1
print(ans%mod)
#print(dic)
