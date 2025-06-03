from collections import Counter
n = int(input())
d = list(input() for _ in range(n))
D = Counter(d)
m = max(D.values())
l = []
for i,j in D.most_common():
  if m != j:
    break
  l.append(i)
l.sort()
for i in l:
  print(i)