import numpy as np
from numpy.fft import rfft, irfft
import sys
input=sys.stdin.readline

N, M = map(int, input().split())
fft_len = 1<<18
MAX = 2*10**5
A = np.zeros(fft_len)
for a in [int(x) for x in input().split()]:
    A[a] += 1
F = rfft(A, fft_len)
f = np.rint(irfft(F*F))
n, ans = 0, 0
for i, c in enumerate(f[:MAX+1][::-1]):
    if M < n+c:
        ans += (M-n)*(MAX-i)
        break
    ans += c*(MAX-i)
    n += c
print(int(ans))
