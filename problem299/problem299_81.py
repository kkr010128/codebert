n=int(input())
a=list(map(int,input().split()))

import numpy as np
x = np.argsort(a)

for i in range(n):
  print(x[i]+1)
