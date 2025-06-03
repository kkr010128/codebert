# B 1%

import math

X = int(input())
Y = 100

cnt = 0
while Y < X:
  cnt += 1
#  Y = math.floor(Y*1.01)
  Y = Y + Y//100

print(cnt)