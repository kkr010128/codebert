x,y = map(int,input().split())
a = (4*x-y)/2
b = (-2*x+y)/2
if a%1 == 0 and 0 <= a and b%1 == 0 and 0 <=b:
  print("Yes")
else:
  print("No")
