a, b = map(int, input().split())
a1 = a/0.08
a2 = (a+1)/0.08

b1 = b/0.1
b2 = (b+1)/0.1


if a1.is_integer():
  x1 = a1
else:
  x1 = a1 + 1
if a2.is_integer():
  x2 = a2
else:
  x2 = a2 + 1
if b1.is_integer():
  y1 = b1
else:
  y1 = b1 + 1
if b2.is_integer():
  y2 = b2
else:
  y2 = b2 + 1
  
s1 = set([i for i in range(int(x1), int(x2))])
s2 = set([i for i in range(int(y1), int(y2))])
s = s1 & s2
if len(s) == 0:
  print(-1)
else:
  print(min(s1 & s2))