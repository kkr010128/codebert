import math
x = int(input())
y = x

while True:
  flg = 0
  for i in range(2,math.ceil(y**0.5)):
    if y%i == 0:
      flg = 1
      break
  if flg == 0:
    print(y)
    break
  y += 1