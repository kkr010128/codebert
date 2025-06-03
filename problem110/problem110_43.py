from itertools import groupby, accumulate, product, permutations, combinations
H, W, K = map(int, input().split())
S = [input() for _ in range(H)]
ans = 0
for p in product([0,1],repeat=H+W):
  cnt = 0
  for i in range(H):
    for j in range(W):
      if S[i][j]=='#' and p[i]==0 and p[H+j]==0:
        cnt += 1
  if cnt == K:
    ans += 1
print(ans)
