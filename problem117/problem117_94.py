# Tsundoku
import numpy as np
N, M, K = map(int,input().split())
A = np.array([0] + list(map(int, input().split())))
B = np.array([0] + list(map(int, input().split())))
a = np.cumsum(A)
b = np.cumsum(B)

ans = 0
j = M

for i in range(N+1):
    if a[i] > K:
        break
    while b[j] > K - a[i]:
        j -= 1
    ans = max(ans, i+j)
    
print(ans)