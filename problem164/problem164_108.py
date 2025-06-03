# B - Battle

import sys

a,b,c,d = map(int,input().split())

while True:
    if c - b <= 0:
        print('Yes')
        sys.exit()
    c = c - b

    if a - d <= 0:
        print('No')
        sys.exit()
    a = a - d
