a,b,c = map(int,input().split())

d = 0

if ( a + b - c )  < 0:
  if ( a + b - c ) ** 2 > 4 * a * b:
    d = 1 
  
if d == 1:
  print("Yes")
else:
  print("No")