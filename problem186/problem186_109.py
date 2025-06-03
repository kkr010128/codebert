K, N = map(int, input().split())
A = list(map(int, input().split()))

import numpy as np

a = np.array(A)
D = np.diff(a)
D = np.append(D, a[0] + K - a[-1])
ind = np.argmax(D)

if N == 2:
    print(a[ind+1]-a[ind])
elif ind == len(a)-1:
    ans =  -a[0] + a[ind]
    print(ans)
else:
    ans = K - (a[ind+1]-a[ind])
    print(ans)
