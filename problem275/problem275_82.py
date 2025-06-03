x,y=map(int,input().split())
d={3:100000,2:200000,1:300000}
r=0
if x<=3:
  r+=d[x]
if y<=3:
  r+=d[y]
if x+y==2:
  r+=400000
print(r)