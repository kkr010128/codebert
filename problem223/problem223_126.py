N,K = list(map(int,input().split()))
P = list(map(int,input().split()))

import numpy as np

Q = np.cumsum(P)

R = np.pad(Q,K,'constant', constant_values=0)[:N]

a = np.argmax(Q-R)

ans = 0
for i in range(K):
    ans += (1.00+P[a-i])/2.00
print(ans)