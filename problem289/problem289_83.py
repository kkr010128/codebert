import math

a,b,x = map(int, input().split())
T=a**2*b

if T//2 < x:
  X= 2*x/a**2 - b
  Y= b - X
  print(math.degrees(math.asin(Y/math.sqrt(a**2+Y**2))))
else:
  X= 2*x/(a*b)
  print(math.degrees(math.asin(b/math.sqrt(X**2+b**2))))