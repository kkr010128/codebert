h = int(input())
w = int(input())
n = int(input())
a = 0
b = 0
c = 0
d = 0
for i in range(h):
  a += w
  b += 1
  if a >= n:
    break
for i in range(w):
  c += h
  d += 1
  if c >= n:
    break
if b > d:
  print(d)
else:
  print(b)