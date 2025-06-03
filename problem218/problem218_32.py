import collections

N = int(input())
cnt = collections.defaultdict(int)

for _ in range(N):
  s = input()
  cnt[s] += 1

max_v = max(cnt.values())
ans   = sorted([k for k, v in cnt.items() if v == max_v])
for s in ans:
  print(s)
