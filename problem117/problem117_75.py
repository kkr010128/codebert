N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

import numpy as np
A0 = [0] + A
B0 = [0] + B
AA = np.cumsum(A0)
BB = np.cumsum(B0)

ans = 0
jmax = M
for i in range(0, N+1):
    a = AA[i]
    if a > K:
        break
    for j in range(jmax, -1, -1):
        b = BB[j]
#        print(a, b)
        if a + b <= K:
            ans = max(ans, i+j)
#            print('ok')
            break
    jmax = j
print(ans)