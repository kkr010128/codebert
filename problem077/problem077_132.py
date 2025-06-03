a, b, c, d = map(int, input().split())
if a == b and c == d:
  print(a*c)
else:
  p1 = a*c
  p2 = a*d
  p3 = b*c
  p4 = b*d
  print(max(p1,p2,p3,p4))