import math
x=int(input())
y=x//100
z=math.ceil((x%100)/5)
if y >= z:
  print(1)
else:
  print(0)
