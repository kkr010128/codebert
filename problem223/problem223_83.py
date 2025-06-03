import bisect,collections,copy,heapq,itertools,math,numpy,string,scipy
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    N,K = LI()
    P = LI()
    Pe = [(v+1)/2 for v in P]
    P_ms = numpy.cumsum(Pe)
    if K==N:print("{:.12f}".format(sum(Pe)));exit(0)
    ans = 0
    for i in range(K,N):
        ans = max(ans,P_ms[i]-P_ms[i-K])
    print("{:.12f}".format(ans))
main()

