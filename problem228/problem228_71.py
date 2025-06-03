import sys
import numpy as np
import math as mt

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
cnt = 1
while n != 1:
  n = n//2
  cnt += 1

print(sum(2**i for i in range(cnt)))
    
