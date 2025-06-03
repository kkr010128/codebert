r, c = map(int, input().split())
l = []
for i in range(r):
  l.append(list(map(int, input().split())))
  l[i] += [sum(l[i])]
  print(*l[i])
l = list(zip(*l))
for i in range(c): print(sum(l[i]), end = " ")
print(sum(l[c]))
