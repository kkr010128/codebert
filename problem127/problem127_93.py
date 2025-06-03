x,y = map(int,input().split())

A  =(-y+4.0*x)/2.0
B = (y-2.0*x)/2.0

if A>=0 and B>=0 and A.is_integer() and B.is_integer():
  print("Yes")
else:
  print("No")