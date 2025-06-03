import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

# b,r = map(str, readline().split())
# A,B = map(int, readline().split())
br = LS()
AB = LI()
U = _S()

def main():
    brAB = zip(br, AB)
    tmp=[]
    for c,n in brAB:
        if c==U:
            tmp.append(n - 1)
        else:
            tmp.append(n)
    return str(tmp[0])+' '+str(tmp[1])
print(main())
