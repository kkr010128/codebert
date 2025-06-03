s = str(input())
t = str(input())
sx = len(s)
tx = len(t)
n = sx - tx + 1
amax = 0
for i in range(n):
  x = 0
  for j in range(tx):
    if s[i+j] == t[j]:
      x += 1
    else:
      pass
  if x > amax:
    amax = x
print(tx - amax)