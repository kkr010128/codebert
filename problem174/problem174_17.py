k=int(input())
from math import gcd
ans=0
for i in range(1,k+1):
  for j in range(1,k+1):
    temp=gcd(i,j)
    for m in range(1,k+1):
      ans=ans+gcd(temp,m)
print(ans)
