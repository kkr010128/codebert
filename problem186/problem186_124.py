k,n=map(int,input().split())
a=sorted(list(map(int, input().split())))
ans=k+a[0]-a[-1]
for i in range(1,n):
    ans=max(ans,a[i]-a[i-1])
print(k-ans)