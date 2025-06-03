import itertools
import math

n=int(input())
d=list(map(int,input().split()))

ans=0
for v in itertools.combinations(d, 2):
  x=v[0]*v[1]
  ans+=x

print(ans)