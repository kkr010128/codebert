import math
N = int(input())
X = N/1.08 
Y = math.ceil(X)
Z = math.floor(Y*1.08)
if N == Z:
  print(Y)
else:
  print(':(')