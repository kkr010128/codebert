import numpy as np
n, *a = map(int, open(0).read().split())
s = np.cumsum(np.array(a))
print(min([abs(s[n - 1] - s[i] - s[i]) for i in range(n - 1)]))
