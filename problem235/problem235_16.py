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
ans = sum(lcm//x for x in A)
print(ans%mod)