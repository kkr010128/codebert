import sys

k, s = sys.stdin.readlines()
k = int(k)
s = s.strip()
if len(s) <= k:
    print(s)
else:
    print('{}...'.format(s[:k]))