import math
n=int(input())
m=int(math.sqrt(n))+1
for i in range(m):
  if n%(m-i)==0:
    k=m-i
    l=n//(m-i)
    break
print(k+l-2)