import math
 
N,D = map(int, input().split())
count = 0
for i in range(0, N):
  x = list(map(int, input().split()))
  if D >= math.sqrt(x[0]**2 + x[1]**2):
    count = count + 1
 
print(count)