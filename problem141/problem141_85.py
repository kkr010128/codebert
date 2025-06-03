n=int(input())
a=list(map(int,input().split()))
if a[0]!=0:
    if n==0 and a[0]==1:
        print(1)
    else:
        print(-1)
    exit()
l=[[] for _ in range(n+1)]
l[0]=[1,1]
l[n]=[a[n],a[n]]
for i in reversed(range(1,n)):
    if l[i+1][0]%2==1:
        l[i]=[l[i+1][0]//2+a[i]+1,l[i+1][1]+a[i]]
    else:
        l[i]=[l[i+1][0]//2+a[i],l[i+1][1]+a[i]]
ans=[0]*(n+1)
ans[0]=1
for i in range(1,n+1):
    if ans[i-1]*2>=l[i][0]:
        ans[i]=min((ans[i-1]-a[i-1])*2,l[i][1])
    else:
        print(-1)
        exit()
print(sum(ans))
