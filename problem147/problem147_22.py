import sys
readline = sys.stdin.buffer.readline
s =readline().rstrip().decode()
t =readline().rstrip().decode()

if t[:-1] == s:
  print('Yes')
else:
  print('No')
