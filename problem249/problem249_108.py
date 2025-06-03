import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    A,B,K = LI()
    A_ans = A-K if A>=K else 0
    B_ans = B-(K-A) if K>A else B
    B_ans = B_ans if B_ans>=0 else 0
    print(A_ans,B_ans)

main()

