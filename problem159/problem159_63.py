import math
X = int(input())
a = 100
for i in range(1,200000):
  a += a//100
  if a >= X:
    break
print(i)