import numpy as np
import math
n=int(input())
a=[]
for i in range(n):
  a.append(list(map(int,input().split())))
a=np.array(a, dtype=object)
ans=0
for i in range(n):
  for j in range(n):
    if i==j:
      continue
    else:
      x= (a[i]-a[j])**2
      hei=math.sqrt(sum(x))
      ans+= hei/n
print(ans)
