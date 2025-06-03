n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
if n==1:
    print(a[0]*2)
    exit()
from bisect import bisect_left,bisect_right
#幸福度がx以上がm以上か？
def f(x):
    global n,a
    ret=0
    for i in range(n):
        ret+=(n-bisect_left(a,x-a[i]))
    return ret
l,r=-1,10**6
while l+1<r:
    k=l+(r-l)//2
    if f(k)>=m:
        l=k
    else:
        r=k
#print(l,r)
#print(f(l),f(r))
if f(r)>=m:
    co,ans=0,0
    for i in range(n):
        co+=(n-bisect_right(a,r-a[i]))
        ans+=(n-bisect_right(a,r-a[i]))*a[i]
    print(2*ans+(m-co)*r)
else:
    co,ans=0,0
    for i in range(n):
        co+=(n-bisect_right(a,l-a[i]))
        ans+=(n-bisect_right(a,l-a[i]))*a[i]
    print(2*ans+(m-co)*l)