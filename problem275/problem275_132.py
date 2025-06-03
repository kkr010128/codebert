x,y=map(int,input().split())
ans=0
x=max(4-x,0)
y=max(4-y,0)
ans+=x*100000+y*100000
if x==3 and y==3:
  ans+=400000
print(ans)