import sys
input=sys.stdin.readline
import math

A,B = (int(x) for x in input().rstrip('\n').split())
c = math.gcd(A,B)
if c==1:
  print(1)
else:
  ps=[]
  d = math.floor(math.sqrt(c))
  for i in range(2,d+2):
    if c%i==0:
      if all(i%x!=0 for x in ps):
        ps.append(i)
        while c % i ==0:
          c = c//i
  if c > 1:
    ps.append(0)
  print(len(ps)+1)