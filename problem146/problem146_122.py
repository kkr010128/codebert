from fractions import gcd

N=int(input())
d={}
#l=[]
MOD = 1000000007
nz=0
for _ in range(N):
    a,b=map(int,input().split())
    if a==0 and b==0:
        nz+=1
        #p=(0,0)
        continue
    elif a==0:
        p=(0,1)
    elif b==0:
        p=(1,0)
    else:
        c=gcd(a,b)
        a,b=a//c,b//c
        if b > 0:
            p=(a,b)
        else: # b < 0
            p=(-a,-b)
    
    #l.append(p)
    if p in d:
        d[p]+=1
    else:
        d[p] = 1

ans=1
#for p in l:
while len(d) > 0:
    p,np=d.popitem()
    if p==(1,0):
        q=(0,1)
    elif p==(0,1):
        q=(1,0)
    else:
        pa,pb=p
        if pa > 0:
            q=(-pb,pa)
        else: #pa < 0
            q=(pb,-pa)
    if q in d:
        nq=d.pop(q)
    else:
        nq=0
    
    ans *= ((2**np + 2**nq - 1) % MOD)
    ans %= MOD

ans -= 1
ans += nz
ans %= MOD
print(ans)