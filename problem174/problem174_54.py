import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)
  
k = int(input())
sum=0
for i in range(1,k+1):
  for j in range(i+1,k+1):
    for l in range(j+1,k+1):
      sum+=6*gcd(i,j,l)
for i in range(1,k+1):
  for j in range (1,k+1):
    sum+=3*gcd(i,j)
sum-=k*(k+1)
print(sum)