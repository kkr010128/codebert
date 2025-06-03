K, N = map(int, input().split())
A = list(map(int, input().split()))

import numpy as np

a = np.array(A)
D = np.diff(a)
D = np.append(D, a[0] + K - a[-1])

print(K - max(D))
