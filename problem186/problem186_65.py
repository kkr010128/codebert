k,n,*a=map(int,open(0).read().split())
dist=10**7
for i in range(n):
    if i==0:
#        print(a[-1]-a[0])
        dist=min(dist,a[-1]-a[0])
    else:
#        print(a[-1+i]+k-a[i])
        dist=min(dist,a[-1+i]+k-a[i])
print(dist)