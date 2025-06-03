import sys 
from functools import reduce
import math
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def gcd(*numbers):
    return reduce(math.gcd, numbers)
K = int(readline())
ans = 0
for i in range(1,K+1):
    for j in range(1,K+1):
        for k in range(1,K+1):
            ans += gcd(i,j,k)
print(ans)