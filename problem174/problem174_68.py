from math import gcd
k=int(input())
cnt=0
for i in range(1,k+1):
  for p in range(1,k+1):
    for q in range(1,k+1):
      gcd1=gcd(i,p)
      
      cnt+=gcd(gcd1,q)
 
      
print(cnt)