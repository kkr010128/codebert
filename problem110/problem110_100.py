h0, w0, k0 = [ int(x) for x in input().split() ]
found, buf = 0, {}
for i in range(h0): buf[1 << i] = { 1 << j for j,x in enumerate(input()) if x == '#' }
for i in range(1, 1 << h0):
  idx = {}
  for k,vs in buf.items():
    if k & i == 0: continue
    for v in vs: idx[v] = idx.get(v, 0) + 1
  for j in range(1, 1 << w0):
    n = sum([ v for k,v in idx.items() if k & j ])
    if n == k0: found += 1
print(found)