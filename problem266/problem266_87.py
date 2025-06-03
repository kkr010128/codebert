ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))
from math import ceil

x=ni()
p=x%100
if ceil(p/5) <= x//100:
  print(1)
else:
  print(0)
