from collections import defaultdict
d = defaultdict(int)
n = int(input())
for _ in range(n): d[input()] += 1
s = sorted(d.items(), key=lambda x: (-x[1], x[0]))
nmax = s[0][1]
for i in s:
  if i[1] != nmax: break
  print(i[0])