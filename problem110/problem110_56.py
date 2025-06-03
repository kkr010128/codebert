h, w, k = map(int, input().split())
fi = []
for _ in range(h):
  s = input()
  fi.append(s)
a = 1 << h
b = 1 << w
ans = 0
for i in range(a * b):
  lh = [0 for _ in range(h)]
  lw = [0 for _ in range(w)]
  for j in range(h):
    if i & (1 << j):
      lh[j] += 1
  for j in range(w):
    if i & (1 << (j + h)):
      lw[j] += 1
  cnt = 0
  for j in range(h):
    for l in range(w):
      if lh[j] == 1:
        continue
      if lw[l] == 1:
        continue
      if fi[j][l] == '#':
        cnt += 1
  if cnt == k:
    ans += 1
print(ans)