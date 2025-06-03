n,m=map(int,input().split())
a=list(map(int,input().split()))
def func(n):
  ret=0
  n=n/2
  while n.is_integer():
    ret+=1
    n=n/2
  return ret
b=func(a[0])
for i in range(1,n):
  if b==func(a[i]):
    continue
  else:
    print(0)
    exit(0)
from fractions import gcd
lcmn=a[0]//2
for i in range(1,n):
    lcmn=(lcmn*a[i]//2)//gcd(lcmn,a[i]//2)
print((1+m//lcmn)//2)
