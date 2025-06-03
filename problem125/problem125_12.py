import math
N= int(input())
if 360%N==0:
  print(int(360/N))
elif 360%N!=0:
  a = math.gcd(360,N)
  print(int(360/a))