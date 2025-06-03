# ABC145 D

X,Y=map(int,input().split())

a,b=-1,-1
if not (2*X-Y)%3:
    b=(2*X-Y)//3
if not (2*Y-X)%3:
    a=(2*Y-X)//3
    



N=10**6
p=10**9+7
f,finv,inv=[0]*N,[0]*N,[0]*N

def nCr_init(L,p):
    for i in range(L+1):
        if i<=1:
            f[i],finv[i],inv[i]=1,1,1
        else:
            f[i]=(f[i-1]*i)%p
            inv[i]=(p-inv[p%i]*(p//i))%p
            finv[i]=(finv[i-1]*inv[i])%p

def nCr(n,r,p):
    if 0<=r<=n and 0<=n:
        return (f[n]*finv[n-r]*finv[r])%p
    else:
        return 0
    
nCr_init(a+b+1,p)
if a>=0 and b>=0:
    print(nCr(a+b,b,p))
else:
    print(0)