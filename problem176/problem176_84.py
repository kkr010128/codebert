import math

def pow(p,n):
    bin_n=bin(n)[2:][::-1]
    tmp=p;pn=1
    for i in range(len(bin_n)):
        if bin_n[i]=="1": pn=(pn*tmp)%mod
        tmp=tmp*tmp%mod
    return pn


mod=10**9+7
n,k=map(int,input().split())

ans=[0]*(k+1)
for i in range(k,0,-1):
    div=set()
    for x in range(1,int(i**0.5)+1):
        if i%x==0: div.add(x);div.add(i//x)
    ans[i]=pow(k//i,n)-sum([ans[j*i] for j in range(k//i,1,-1)])
    ans[i]%=mod
print(sum(ans[i]*i for i in range(k+1))%mod)