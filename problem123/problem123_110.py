n = int(input())
a = list(map(int, input().split()))

m = max(a)
ans = [0] * n
z = 1
while True:
  b = False
  for i in range(n):
    if a[i] & z:
      b = not b
  for i in range(n):
    if not b:
      if a[i] & z:
        ans[i] |= z
    else:
      if not (a[i] & z):
        ans[i] |= z

  z <<= 1
  if z > m:
    break

print(' '.join([str(x) for x in ans]))