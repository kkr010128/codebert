n=int(input())
a=list(map(int,input().split()))
cnt=0
ans=1000
for i in range(1,n):
    if a[i-1]<a[i]:
        cnt+=ans//a[i-1]
        ans-=cnt*a[i-1]
        ans+=cnt*a[i]
        cnt=0
print(ans)