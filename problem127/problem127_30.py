x,y=map(int,input().split())
a=(4*x-y)/2
b=(2*x-y)/(-2)
if a>=0 and b>=0 and a.is_integer() and b.is_integer():
  print("Yes")
else:
  print("No")