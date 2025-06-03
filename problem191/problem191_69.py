l=int(input())

import numpy as np
result = 0
for x in np.arange(l/3-0.1, l/3+0.1, 0.1):
  for y in np.arange(x, l/3+0.1, 0.1):
    z = l - (x+y)
    if z <= 0:
      break
    v = x*y*z
    result = max(v, result)
print(result)