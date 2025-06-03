x,y=map(int,input().split())
if (x+y)%3!=0:
    print(0)
    exit()
if x<y:
    x,y=y,x
if 2*y<x:
    print(0)
    exit()
mod=10**9+7
a=(2*y-x)//3
b=(2*x-y)//3
mx=10**6
k=[1]*(mx+1)
def inv(n):
    return pow(n,mod-2,mod)
for i in range(mx):
    k[i+1]=k[i]*(i+1)%mod
ans=(k[a+b]*inv(k[a])*inv(k[b]))%mod
print(ans)