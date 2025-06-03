from fractions import gcd
from functools import reduce
def l(a,b):return a*b//gcd(a,b)
def L(N):return reduce(l,N)
n,m=map(int,input().split())
A=list(map(lambda x:int(x)//2,input().split()))
a=A[0]
c=0
while(a%2==0):
  a//=2
  c+=1
if any([(a%(2**c)==0 and a//(2**c))%2==0 for a in A]):
  print(0)
  exit()
a=L(A)
print((m+a)//(2*a))
