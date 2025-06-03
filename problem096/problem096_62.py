import math

N, D = map(int, input().split())
count = 0

for i in range(N):
  x, y = map(int, input().split())
  d = math.sqrt(x**2 + y**2)
  
  if d<=D:
    count += 1
    
print(count)
