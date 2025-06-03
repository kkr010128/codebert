import math
A,B,C,D = map(int, input().split()) 

Taka=A/D
Aoki=C/B

if math.ceil(Taka)>=math.ceil(Aoki):
  print("Yes")
else:
  print("No")