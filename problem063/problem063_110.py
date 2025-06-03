import sys
import math

char = "abcdefghijklmnopqrstuvwxyz"

cnt = {}

for S in sys.stdin:
    for x in S:
        x = x.lower()
        if x not in cnt:
            cnt[x] = 0
        cnt[x] += 1
    
for c in char:
    sys.stdout.write(c + " : ")
    if c not in cnt:
        print 0
    else:
        print cnt[c]