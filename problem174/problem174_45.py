import math
K = int(input())
S = 0
for a in range(1, K+1):
  for b in range(1, K+1):
    T = math.gcd(a, b)
    for c in range(1, K+1):
      S += math.gcd(T, c)
print(S)