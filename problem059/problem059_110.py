r, c = map(int, [int(_) for _ in input().split()])

ll = []

for _ in range(r):
  l =  [int(n) for n in input().split()]
  l.append(sum(l))
  ll.append(l)

l = [sum(_) for _ in zip(*ll)]
ll.append(l)

for l in ll:
  print(" ".join([str(_) for _ in l]))