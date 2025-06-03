import sys
a,v = map(int, sys.stdin.readline().rstrip("\n").split())
b,w = map(int, sys.stdin.readline().rstrip("\n").split())
t = int(sys.stdin.readline().rstrip("\n"))
between = abs(b - a)
speed = v-w
if between <= speed*t:
  print('YES')
else:
  print('NO')