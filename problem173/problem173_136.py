import sys 
import numpy as np
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = int(readline())
ans = 0
for i in range(1,N+1):
    if i % 3 == 0 or i % 5 == 0:
        continue
    ans += i
print(ans)