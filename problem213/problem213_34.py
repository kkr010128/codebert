n = int(input())
a = [int(i) for i in input().split()]
#import numpy as np
#n = 100
#a = np.random.randint(1, 100, n)
a = sorted(a)
minsum = float('inf')
for i in range(a[0], a[-1]+1):
  cnt = 0
  for ai in a:
    cnt += (ai - i)**2
  if cnt <= minsum:
    minsum = cnt
print(minsum)