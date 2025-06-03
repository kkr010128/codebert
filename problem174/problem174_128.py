import math
k=int(input())
s=0
for a in range(k):
  for b in range(k):
    x=math.gcd(a+1,b+1)
    for c in range(k):
      s+=math.gcd(x,c+1)
print(s)