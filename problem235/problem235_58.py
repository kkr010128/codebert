import sys 
from functools import reduce
from math import gcd
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
mod = 10 ** 9 + 7
N = int(readline())
A = list(map(int,readline().split()))
lcm = reduce(lambda x,y:x*y//gcd(x,y),A)
ans = 0
coef = sum(pow(x,mod-2,mod) for x in A)
ans = lcm * coef % mod
print(ans)