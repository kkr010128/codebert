import numpy as np
n = int(input())
cnt = 0

for k in range(1,n+1):
    d = n//k
    if d == 1:
        cnt += (k+n)*(n-k+1)//2
        break
    cnt += k*d*(d+1)//2
print(cnt)