A,B,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
for i in range(m):
  x,y,c=map(int,input().split())
  l.append(a[x-1]+b[y-1]-c)
l.append(min(a)+min(b))
print(min(l))