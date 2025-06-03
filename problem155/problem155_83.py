n,m=map(int,input().split())
h=list(map(int,input().split()))
x=[0]*n
y=[0]*n
for i in range(m):
    a,b=map(int,input().split())
    x[a-1]+=1
    x[b-1]+=1
    if h[a-1]>h[b-1]:
        y[a-1]+=1
    elif h[b-1]>h[a-1]:
        y[b-1]+=1
ans=0
for i in range(n):
    if x[i]==y[i]:
        ans+=1
print(ans)