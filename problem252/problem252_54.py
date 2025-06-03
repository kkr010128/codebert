import numpy as np
from numpy.fft import fft
from numpy.fft import ifft
class FFT:
  def exe(s, A, B):
    N, M = 1, len(A) + len(B) - 1
    while N < M: N <<= 1
    A, B = s.arrN(N, A), s.arrN(N, B)
    A = fft(A) * fft(B)
    A = ifft(A).real[:M] + 0.5
    return list(map(int, A))
  def arrN(s, N, L):
    return np.zeros(N) + (L + [0] * (N - len(L)))

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

MAX = max(A)
L = [0] * (MAX + 1)
for i in A:
  L[i] += 1

f = FFT()
L = f.exe(L, L)

ans = 0
for i in range(len(L) - 1, -1, -1):
  if L[i] < M:
    ans += i * L[i]
    M -= L[i]
  else:
    ans += i * M
    break

print(ans)