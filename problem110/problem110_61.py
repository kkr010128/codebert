h, w, k = map(int, input().split())
X = [[1 if a == "#" else 0 for a in input()] for _ in range(h)]
ans = 0
for ii in range(1 << h):
  for jj in range(1 << w):
    if sum([sum([X[i][j] for j in range(w) if jj >> j & 1]) for i in range(h) if ii >> i & 1]) == k:
      ans += 1
print(ans)