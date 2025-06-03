x,y=map(int,input().split())
a=(y-2*x)//2
b=x-a
 
if y%2==0 and a>=0 and b>=0:
  print("Yes")
else:
  print("No")