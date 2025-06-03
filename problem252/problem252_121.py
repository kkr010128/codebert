import numpy as np
from numpy.fft import rfft, irfft
N,M = list(map(int,input().split()))
A = list(map(int,input().split()))
X = np.zeros(10**5+1)
l = 2*(10**5)+10
for i in range(N):
    X[A[i]] += 1
data = np.rint(irfft(rfft(X, l)**2 ))
num = 0
ans = 0
for i in range(len(data) -1 ,0,-1):
    if data[i] != 0:
        if num + data[i] >= M:
            ans += (M - num) * i
            break
        else:
            ans += data[i]*i
            num += data[i]
print(int(ans))