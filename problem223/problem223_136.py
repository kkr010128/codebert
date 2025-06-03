N, K = map(int, input().split())
p = list(map(int, input().split()))

import numpy as np

data = np.array(p) + 1

Pcum = np.zeros(N + 1, np.int32)
Pcum[1:] = data.cumsum()

length_K_sums = Pcum[K:] - Pcum[0:-K]

print(np.max(length_K_sums)/2)
