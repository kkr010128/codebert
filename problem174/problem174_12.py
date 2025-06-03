import math
n=int(input())
l=0
summ=0
for i in range(1,n+1):
  for j in range(1,n+1):
    for k in range(1,n+1):
      ans=math.gcd(i,j,)
      ans=math.gcd(ans,k)
      summ+=ans
print(summ)