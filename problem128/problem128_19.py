x, n = map(int, input().split())
if n == 0:
  print(x)
  exit(0)
p = list(map(int, input().split()))
a = [i for i in range(201)]
b = sorted(list(set(a) - set(p)))
min_v = 1000
min_id = 0
for i in range(len(b)):
  if abs(x - b[i]) < min_v:
    min_v = abs(x - b[i])
    min_id = i
print(b[min_id])