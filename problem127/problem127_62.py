x,y=map(int,input().split())
t=2*y-4*x
c=y-t
if t<0 or c<0 or t%4!=0 or c%2!=0:
  print("No")
else:
  print("Yes")
