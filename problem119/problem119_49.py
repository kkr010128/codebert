import sys
import numpy as np
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
# ----------------------------------------------
aa = str(input())
#print(aa)
tar = ord(aa)
if (tar <= 91):
    print('A')
else:
    print('a')
