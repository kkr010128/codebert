n, k = map(int, input().split())
a = list(map(int, input().split()))

inf = 1
sup = max(a)

while inf < sup:
  x = (inf + sup) // 2
  cut = 0
  for a_i in a:
    cut += (a_i - 1) // x
  if cut <= k:
    sup = x
  else:
    inf = x + 1
print(sup)