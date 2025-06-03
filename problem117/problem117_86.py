n, m, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

As = [0] * (n + 1)
Bs = [0] * (m + 1)
for i in range(n):
  As[i + 1] = A[i] + As[i]
for i in range(m):
  Bs[i + 1] = B[i] + Bs[i]

l = 0
r = n + m + 1
while r - l > 1:
  p = (l + r) // 2
  best = min(
    As[i] + Bs[p - i] for i in range(p + 1)
    if min(i, n) + min(p - i, m) == p
  )
  if best <= k:
    l = p
  else:
    r = p
print(l)