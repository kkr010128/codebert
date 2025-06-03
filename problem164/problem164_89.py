a, b, c, d = map(int,input().split())
t = c//b
if not c % b == 0:
  t += 1
o = a//d
if not a % d == 0:
  o += 1

if t <= o:
  print('Yes')
else:
  print('No')