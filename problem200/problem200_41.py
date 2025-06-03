a,b,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=[list(map(int,input().split())) for _ in range(m)]

ans=min(a)+min(b)
for i in range(m):
  ans=min(ans,(a[x[i][0]-1]+b[x[i][1]-1]-x[i][2]))

print(ans)
