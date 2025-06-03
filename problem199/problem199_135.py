import sys
s = input()

def match(a):
  if a[0:2] == 'hi':
    return a[2:]
  else:
    print('No')
    sys.exit()
if len(s)%2 == 1:
  print('No')
  sys.exit()
else:
  while len(s) > 1:
    s = match(s)
  print('Yes')