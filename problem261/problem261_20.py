import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    S = _S()
    ans = 0
    for i in range(int(len(S)/2)):
        if S[i]==S[-i-1]:
            continue
        else:
            ans +=1
    print(ans)

main()

