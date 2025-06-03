N = int(input())
A = list(map(int, input().split()))
mod = int(1e+9 + 7)
L = A[0]
def inved(a):
  x, y, u, v, k, l = 1, 0, 0, 1, a, mod
  while l != 0:
    x, y, u, v = u, v, x - u * (k // l), y - v * (k // l)
    k, l = l, k % l
  return x % mod
for i in range(N-1):
  a, b = L, A[i+1]
  while b != 0:
    a, b = b, a % b
  b = A[i+1] // a
  L = b * L
L %= mod
S = 0
for i in range(N):
  S += inved(A[i])
  S %= mod
S *= L
S %= mod
print(S)