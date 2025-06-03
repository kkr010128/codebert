k,n=map(int,input().split())
a=[int(i) for i in input().split()]

saitanhiku=a[2]-a[1]
for i in range(n-1):
    if a[i+1]-a[i]>=saitanhiku:
        saitanhiku=a[i+1]-a[i]
if (k-a[n-1])+a[0]>=saitanhiku:
    saitanhiku=k-a[n-1]+a[0]
print(k-saitanhiku)