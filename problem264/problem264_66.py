from sys import stdin
m1, d1 = [int(_) for _ in stdin.readline().rstrip().split()]
m2, d2 = [int(_) for _ in stdin.readline().rstrip().split()]
if m1 == m2:
  print(0)
else:
  print(1)