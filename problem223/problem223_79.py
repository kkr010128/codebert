n, k = map(int, input().split())
p = [int(i) for i in input().split()]
q = 0
for i in range(k):
  q += p[i]
r = q
for i in range(n - k):
  r -= p[i]
  r += p[i + k]
  if r > q:
    q = r
print((q + k) / 2)