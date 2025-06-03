import math
k = int(input())
su = 0
lis = []
for x in range(1, k+1):
  for y in range(1, k+1):
    a = math.gcd(x, y)
    lis.append(a)

for z in range(1, k+1):
  for p in lis:
    ans = math.gcd(p, z)
    su += ans
  
print(su)