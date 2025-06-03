import numpy as np
n,m = map(int, input().split())
h = np.array([int(i) for i in input().split()])
h_i = np.ones((n))
for i in range(m):
    a,b = map(int, input().split())
    if h[a-1] < h[b-1]:
        h_i[a-1] = 0
    elif h[b-1] < h[a-1]:
        h_i[b-1] = 0
    elif h[a-1] == h[b-1]:
        h_i[a-1] = 0
        h_i[b-1] = 0
ans = (h_i > 0).sum()
print(ans)