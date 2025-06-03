N = int(input())
from functools import reduce
import math
sum=0
for i in range(1,N+1):
  for j in range(1,N+1):
    a = math.gcd(i,j)
    for k in range(1,N+1):
      sum+=math.gcd(a,k)
print(sum)      