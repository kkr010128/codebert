import math
K = int(input())
ans = 0
for i in range(K):
  for t in range(K):
    for j in range(K):
      gcd1 = math.gcd(i+1,t+1)
      gcd2 = math.gcd(gcd1,j+1)
      ans += gcd2
print(ans)