import math
N = float(input())
if(N%2==0):
  print(1/2)
else:
  print((math.floor(N/2)+1)/N)