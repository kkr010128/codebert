import numpy as np
N, M = list(map(int, input().split()))
A = [int(_) for _ in input().split()]
x = np.zeros(2 ** 18)
for a in A:
  x[a] += 1

y = np.fft.fft(x)

for k in range(len(y)):
  y[k] *= y[k]

x = np.fft.ifft(y).real

happiness = 0
for i in reversed(range(0, len(x))):
  happiness += i * min(int(x[i] + 0.5), M)
  M -= int(x[i] + 0.5)
  if M <= 0:
    break

print(happiness)