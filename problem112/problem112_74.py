from decimal import *

n,k = map(int,input().split())
a = list(map(int,input().split()))
MOD = 10**9 + 7

ze = []
pl,mi = [],[]
for i in range(n):
    if a[i] < 0:
        ze.append((-a[i],1))
        mi.append(a[i])
    else:
        ze.append((a[i],0))
        pl.append(a[i])
        
ze.sort(reverse = True)
pl.sort(reverse = True)
mi.sort()

one = 0
for i in range(k):
    one += ze[i][1]
    
ans = 1
zero = k-one

if one % 2 == 0:
    for i in range(k):
        ans = ans * ze[i][0] % MOD
    print(ans)
        
elif len(pl) == 0:
    for i in range(k):
        ans = ans * mi[n-1-i] % MOD
    print(ans)
        
else:
    if (zero == len(pl) and one == len(mi)) or len(pl) == 0 or len(mi) == 0:
        ak = [zero,one]
    elif (zero != len(pl) and one == len(mi)) or zero == 0:
        ak = [zero+1,one-1]
    elif zero == len(pl) and one != len(mi) or one == 0:
        ak = [zero-1,one+1]
    else:
        if Decimal(abs(mi[one]))/Decimal(pl[zero-1]) >= Decimal(pl[zero])/Decimal(abs(mi[one-1])):
            ak = [zero-1,one+1]
        else:
            ak = [zero+1,one-1]
            
    ans = 1
    for i in range(ak[0]):
        ans = ans * pl[i] % MOD
    for i in range(ak[1]):
        ans = ans * mi[i] % MOD
        
    print(ans)