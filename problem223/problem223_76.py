import bisect,collections,copy,heapq,itertools,math,string
import numpy as np
import sys
sys.setrecursionlimit(10**7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

N,K = LI()
p = LI()
E_half = np.array(p) + 1

def main():
    Pcum = np.zeros(N + 1, np.int32)
    Pcum[1:] = E_half.cumsum()
    # print(E_half)
    # print(Pcum)
    partial_sums_E_half = np.zeros(N-K+1, np.int32)
    for i in range(N-K+1):
        partial_sums_E_half[i] = Pcum[i+K] - Pcum[i]

    # partial_sums = Pcum[K:] - Pcum[0:-K]
    return (partial_sums_E_half.max())/2
print(main())
