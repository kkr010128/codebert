from math import gcd
K = int(input())
goukei = 0
for a in range(1,K+1):
  for b in range(1,K+1):
    G = gcd(a,b)
    for c in range(1,K+1):
      goukei += gcd(G,c)
print(goukei)