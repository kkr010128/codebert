import math
a, b = map(int, input().split())
for i in range(1251):
  tax8 = math.floor(i * 0.08)
  tax10 = math.floor(i * 0.1)
  if (tax8, tax10) == (a, b): 
    print(i)
    break
else:
  print(-1)