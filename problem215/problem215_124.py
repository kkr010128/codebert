n,k=map(int,input().split())
mi = min(n-1,k)
di = 10**9+7
def pow_k(x,i):
    if i==0:
        return 0
    K=1
    while i>1:
        if i % 2 != 0:
            K = (K*x)%di
        x = (x*x)%di
        i //= 2

    return (K * x)%di

lis = [i for i in range(n+1)]
lisr = [i for i in range(n+1)]
lis[0]=1
for i in range(1,n+1):
    lis[i]=(lis[i-1]*lis[i])%di
    lisr[i] = pow_k(lisr[i],di-2)

lisr[0]=1
for i in range(1,n+1):
    lisr[i]=(lisr[i-1]*lisr[i])%di

#print(lis,lisr)

su = 1
for i in range(1,mi+1):
    pl = ((((lis[n-1]*lisr[i])%di)*lisr[n-1-i])%di)
    plu = (pl*((((lis[n]*lisr[i])%di)*lisr[n-i])%di))%di
    su+=plu
    su%=di
print(su)
