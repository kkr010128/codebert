r, c = map(int, input().split())
output = []
for _ in range(r):
  l = list(map(int, input().split()))
  s = sum(l)
  l.append(s)
  output.append(l)
final = []
for i in range(c):
  t = 0
  for j in range(r):
    t += output[j][i]
  final.append(t)
s = sum(final)
final.append(s)
output.append(final)
for i in output:
  print(*i)
