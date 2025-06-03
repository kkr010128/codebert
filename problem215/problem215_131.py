x=input().split()
n=int(x[0])
k=int(x[1])
def fact_inverse(n,p):
    fact=[1]*(n+1)
    inv=[1]*(n+1)
    inv_fact=[1]*(n+1)
    inv[0]=0
    inv_fact[0]=0
    for i in range(2,n+1):
        fact[i]=(fact[i-1]*i)%p
        #compute the inverse of i mod p
        inv[i]=(-inv[p%i]*(p//i))%p
        inv_fact[i]=(inv_fact[i-1]*inv[i])%p
    return fact,inv_fact    
    

def combi2(n,p):
    f,inv=fact_inverse(n,p)
    combis=[1]*(n+1)
    for k in range(1,n+1):
        if k >=n//2+1:
            combis[k]=combis[n-k]
        else:
            combis[k]=(((f[n]*inv[n-k])%p)*inv[k])%p
    return combis    
      
    
p=10**9+7
combis1=combi2(n,p)
combis2=combi2(n-1,p)
s=0
L=min(n,k+1)
for i in range(L):
  s=(s+(combis1[i]*combis2[i])%p)%p
print(s)  
