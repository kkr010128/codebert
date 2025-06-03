import sys
import numpy as np
import math as mt

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, a, b = map(int, readline().split())

ans = a * (n//(a + b))
if n%(a+b) < a:
  ans += n%(a+b)
else:
  ans += a
print(ans)

    
