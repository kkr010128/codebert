import math
l,r,d=map(int,input().split())
i=math.ceil(l/d)
c=0
while((d*i)>=l and (d*i)<=r):
  c+=1
  i+=1
print(c)