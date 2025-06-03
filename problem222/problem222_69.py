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
N = I()
A = LI()

def main():
    judge=False
    if len(set(A))==N:
        judge=True
    if judge:
        return 'YES'
    else:
        return 'NO'
print(main())
