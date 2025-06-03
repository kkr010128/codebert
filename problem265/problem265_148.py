n = int(input())
import math
for i in range (50000):
  x = i*1.08
  if math.floor(x) == n:
    print(i)
    exit()
print(":(")