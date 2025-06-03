n, q = map(int, input().split())
l = []
for i in range(n):
  t = []
  for j in input().split():
    t += [j]
  t[1] = int(t[1])
  l += [t]

c = 0
while len(l) > 0:
  if l[0][1] > q:
    l[0][1] -= q
    l += [l[0]]
    l.pop(0)
    c += q
  else:
    c += l[0][1]
    print(l[0][0], c)
    l.pop(0)
