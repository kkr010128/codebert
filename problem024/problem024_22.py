[n, k] = map(int, input().split(' '))
wi = list(map(int, [input() for i in range(n)]))

def isAllocatable(p):
  kw, ki = 0, 1
  for w in wi:
    if w > p: return False
    kw += w
    if kw <= p: continue
    ki += 1
    if k < ki: return False
    kw = w
  return True

l = 0
r = sum(wi)
while l + 1 < r:
  p = int((l + r) / 2)
  if isAllocatable(p): r = p
  else: l = p
print(r)

