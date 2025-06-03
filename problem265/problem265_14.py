import math

N = int(input())

lower = N / 1.08

vl = math.ceil(lower)

if math.floor(vl * 1.08) == N:
  print(vl)
else:
  print(":(")