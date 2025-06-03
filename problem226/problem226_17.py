import math
a,b=map(int,input().split())
A=[int(x) for x in input().split()]
if a<=sum(A):
  print("Yes")
else:
  print("No")