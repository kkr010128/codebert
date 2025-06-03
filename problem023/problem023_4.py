import sys
d = {}

n = int(input())
for i in sys.stdin:
    q, c = i.split()
    if q == 'find':
        if c in d:
            print('yes')
        else:
            print('no')

    else:
        d[c] = True
