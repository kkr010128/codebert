def min(a,i):
  x = a[0]
  for t in range(0, i):
    if x > a[t]:
      x = a[t]
  return x

def max(a,i):
  y = a[0]
  for t in range(0, i):
    if y < a[t]:
      y = a[t]
  return y

def sum(a,i):
  s = 0
  for t in range(0, i):
    s += a[t]
  return s

i = int(raw_input())
a = map(int, raw_input().split())
print "%d %d %d" % (min(a,i), max(a,i), sum(a,i))