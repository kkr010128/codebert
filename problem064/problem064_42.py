import sys

s = sys.stdin.readline().rstrip('\r\n')
p = sys.stdin.readline().rstrip('\r\n')

s += s
if p in s:
  print('Yes')
else:
  print('No')

