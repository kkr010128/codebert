n,m=map(int,input().split())
h=list(map(int,input().split()))
ans=[1]*n

for i in range(m):
    a,b=map(int,input().split())
    a,b,=a-1,b-1
    if h[a]==h[b]:
        ans[a],ans[b]=0,0
    elif h[a]>h[b]:
        ans[b]=0
    else:
        ans[a]=0
print(ans.count(1))
