import numpy as np

a, b = map(int, input().split())
ans = np.lcm(a, b)
print(ans)