N=int(input())
xy=[tuple(map(int,input().split())) for _ in range(N)]
ans=0
zmi=10**10
zma=-10**10
wmi=10**10
wma=-10**10
for x,y in xy:
    zmi=min(zmi,x+y)
    zma=max(zma,x+y)
    wmi=min(wmi,x-y)
    wma=max(wma,x-y)
print(max(zma-zmi,wma-wmi))