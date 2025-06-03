h, w, k = map(int, input().split())
c = []
for i in range(h):
  c.append(input())
t = 2**(h+w)
ans = 0
for i in range(t):
  tc = c[:]
  b = format(i, 'b').zfill(h+w)
  for j in range(len(b)):
    if b[j] == "1":
      if j < h:
        tc[j] = "?"*w
      else:
        for l in range(h):
          tc[l] = tc[l][:(j-h)] + "?" + tc[l][(j-h+1):]
  cn = 0
  for j in range(h):
    cn += tc[j].count("#")
  if cn == k:
    ans += 1
print(ans)