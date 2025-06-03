mod=10**9+7
x,y=map(int,input().split())
if (x+y)%3!=0:
    print(0)
    exit()
a=min(x,y)
b=max(x,y)
if 2*a<b:
    print(0)
    exit()

k=(x+y)//3
left_x=2*k
left_y=k
r=left_x-x

def factorialmod(n,mod):
    ans=1
    for i in range(2,n+1):
        ans*=i
        ans%=mod
    return ans

fac_k=factorialmod(k,mod)
fac_k_r=factorialmod(k-r,mod)
fac_r=factorialmod(r,mod)
bunbo=fac_k_r*fac_r%mod
print(fac_k*pow(bunbo,mod-2,mod)%mod)