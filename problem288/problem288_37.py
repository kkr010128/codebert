n=int(input())
import math
for i in range(int(math.sqrt(n)),0,-1):
  if n%i==0:
    print(i+n//i-2)
    break