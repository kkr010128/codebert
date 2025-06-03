t1,t2=map(int,input().split())
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
x=(a1-b1)*t1
y=(a2-b2)*t2
if x>0:
  x*=-1
  y*=-1
if x+y<0:print(0)
elif x+y==0:print("infinity")
else:
  ans=(-x)//(x+y)
  if (-x)%(x+y):print(ans*2+1)
  else:print(ans*2)