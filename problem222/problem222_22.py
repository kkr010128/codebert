N=int(input())
from collections import Counter
if max(Counter([int(x) for x in input().split()]).values())==1:
  print("YES")
else:
  print("NO")