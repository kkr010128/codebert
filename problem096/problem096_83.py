import math
count = 0
n,d = (int(x) for x in input().split())

for i in range(n):
  x,y = (int(x) for x in input().split())
  result = math.sqrt(x * x + y * y) 
  if result <= d:
    count += 1

print(count)