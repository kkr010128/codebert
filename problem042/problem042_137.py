import sys
for i, x in enumerate(map(int, sys.stdin)):
  if x == 0 or not x:
    break;
  print('Case {0}: {1}'.format(i + 1, x))