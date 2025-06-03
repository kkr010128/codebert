import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    N = I()
    S = _S()
    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    ans = ""
    for s in S:
        ind = (alpha.index(s)+N) if (alpha.index(s)+N)<26 else (alpha.index(s)+N)-26
        ans += alpha[ind]
    print(ans)


main()

