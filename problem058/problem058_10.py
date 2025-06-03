import sys
import math

while 1:
    n, x = map(int , raw_input().split())
    
    if n + x == 0:
        break

    cnt = 0
    for i in xrange(1, n+1):
        for j in xrange(i+1, n+1):
            for k in xrange(j+1, n+1):
                if i + j + k == x:
                    cnt += 1

    print cnt