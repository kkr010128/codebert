a,b,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
ans=min(x)+min(y)
for i in range(m):
  q,w,e=map(int,input().split())
  ans=min(ans,x[q-1]+y[w-1]-e)
print(ans)