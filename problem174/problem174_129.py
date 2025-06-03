import math
K = int(input())
 
# gcd(a, b, c)=gcd(gcd(a,b), c) が成り立つ
s = 0
for a in range(1, K+1):
  for b in range(1, K+1):
    d = math.gcd(a, b) # gcd(a, b)は先に計算しておく
    for c in range(1, K+1):
      s += math.gcd(d, c)
      
print(s)