import math
k = int(input())
ans =0
da =0
for i in range(1,k+1):
  for j in range(1,k+1):
    for n in range(1,k+1):
      da = math.gcd(i,j)
      ans += math.gcd(da,n)
print(ans)