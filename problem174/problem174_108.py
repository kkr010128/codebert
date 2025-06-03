import math

N=int(input())
sum=0
for i in range(1,N+1):
  for j in range(1,N+1):
    x=math.gcd(i,j)
    for k in range(1,N+1):
      y=math.gcd(x,k)
      sum = sum+y
print(sum)