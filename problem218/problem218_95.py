N = int(input())
d = {}
for i in range(N):
  s = input()
  if s in d.keys():
    d[s] += 1
  else:
    d[s] = 1
mx = 0
for i in d.values():
  mx = max(mx, i)
for i in sorted(d.items()):
  if i[1] == mx:
    print(i[0])