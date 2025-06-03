n=int(input())
a=list(map(int,input().split()))+[0]
b=[0]*(n+1)
b[0]=1-a[0]
r=sum(a)-a[0]-a[1]
for i in range(1,n+1):
    b[i]=min(r,b[i-1]*2-a[i])
    r-=a[i+1]
if any(i<0 for i in b):print(-1)
else:print(sum(a)+sum(b))