def median(q):
  l = len(q)
  q = sorted(q, reverse=True)
  if l%2 == 0:
    return (q[int(l/2)] + q[int(l/2)-1])/2
  else:
    return q[int((l+1)/2-1)]
n = int(input())

a = []
b = []
for i in range(n):
  x, y = map(int, input().split())
  a.append(x)
  b.append(y)
med_a = median(a)
med_b = median(b)

if n%2 == 0:
  print(int(2*(med_b - med_a) + 1))
else:
  print((med_b - med_a) + 1)