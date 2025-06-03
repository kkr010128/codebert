import sys 
import numpy as np
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = readline().decode().rstrip()
if '7' in N:
    print('Yes')
else:
    print('No')