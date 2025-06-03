n = int(input())
d = {}

for i in range(n):
  s = str(input())
  if s in d.keys():
    d[s] += 1
  else:
    d[s] = 1

max_count = max(d.values())

for i in sorted(d.keys()):
  if d[i] == max_count:
    print(i)