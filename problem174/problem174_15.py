import math
n=int(input())

ans=0
for a in range(1,n+1):
  for b in range(1,n+1):
    d=math.gcd(a,b)
    if d==1:
      ans+=n
      continue
    if d==2:
      ans+=n//2*3+n%2
      continue
    if d==3:
      ans+=n//3*5+n%3
      continue
    if d==5:
      ans+=n//5*9+n%5
      continue
    for c in range(1,n+1):
      ans += math.gcd(c,d)

print(ans)