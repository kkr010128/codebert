k,n=map(int,input().split())
a=list(map(int,input().split()))
res=k-a[-1]+a[0]
for i in range(n-1):
    res=max(res,abs(a[i]-a[i+1]))
print(k-res)