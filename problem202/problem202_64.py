N, A, B = map(int, input().split())

s = N // (A+B)

t = N % (A+B)

k = 0

if t <= A:
  k = t
else:
  k = A

print(s*A+k)