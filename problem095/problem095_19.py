import sys

X = int(input())

if X >= 30:
    print('Yes')
else:
    print('No')

print('Yes\nNo', file=sys.stderr)
