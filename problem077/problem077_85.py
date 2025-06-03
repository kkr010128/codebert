import numpy as np
a = list(map(int, input().split()))
ans = -1*float('inf')
y = np.array(a[2:])
for i in a[:2]:
  ans = max(ans, max(i*y))
print(ans)