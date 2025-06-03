import math
n=int(input())
ans=-1
for x in range(0,50000):
  if n==math.floor(x*1.08):
    ans=x
    break
if ans==-1:
  print(":(")
else:
  print(ans)