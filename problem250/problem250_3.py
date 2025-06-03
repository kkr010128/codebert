import math
x = int(input())
ans = x
flag = True
while True:
  flag = True
  for i in range(2, math.floor(math.sqrt(ans))):
    if ans % i ==0:
      ans += 1
      flag = False
      break
  if flag:
    print(ans)
    break