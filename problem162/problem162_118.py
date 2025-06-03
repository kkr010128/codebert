N, M = list(map(int, input().split()))

import math
ans = []
if M == 1:
    ans.append((1, 2))
else:
    m0 = (1, M+1)
    m1 = (M+2, 2*M+1)
    for _ in range(math.ceil(M/2)):
        if m0[0] < m0[1]:
            ans.append(m0)
        if m1[0] < m1[1]:
            ans.append(m1)
        m0 = (m0[0]+1, m0[1]-1)
        m1 = (m1[0]+1, m1[1]-1)

for a in ans:
    print(a[0], a[1])
