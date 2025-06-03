n, k = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(k)]
mod = 998244353

dp = [1]
acc = [0, 1]

for i in range(1, n):
  new = 0
  for l, r in LR:
    if i < l:
      continue
    r = min(r, i)
    new += acc[i-l+1] - acc[i-r]
    new %= mod
  dp.append(new)
  acc.append((acc[-1]+new) % mod)

print(dp[-1])