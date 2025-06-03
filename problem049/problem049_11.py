import sys
import os
 
 
for line in sys.stdin:
    H, W = map(int, line.split())
    if H == 0 and W == 0:
        break
    print(('#' * W + '\n') * H)
