from fractions import gcd
def lcm(p, q):
  return (p * q // int(gcd(p, q)))
N, M = map(int, input().split())
A = list(map(int,input().split()))
B = []
for i in range(N):
  b = 0
  while A[i] % 2 == 0:
    A[i] >>= 1
    b += 1
  B.append(b)
S = set(B)
if len(S) != 1:
  print(0)
else:
  P = 1
  for i in range(N):
    P = lcm(P, A[i])
  print((M // (2 ** (list(S)[0] - 1)) + P) // (2 * P))