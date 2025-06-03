from functools import reduce
import sys

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int,LS()))

N = I()
a = LI()

xor_reduce = reduce(lambda x,y:x ^ y, a)
ans = [str(xor_reduce ^ x) for x in a]
print(*ans)