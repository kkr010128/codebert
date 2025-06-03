from heapq import *
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    n=II()
    ss=[SI() for _ in range(n)]
    ms1=[]
    ms2=[]
    for s in ss:
        mn=0
        now=0
        for c in s:
            if c=="(":now+=1
            else:now-=1
            if now<mn:mn=now
        if now>0:ms1.append((mn,now))
        else:ms2.append((mn-now,-now))
    #print(ms1)
    #print(ms2)

    cnt=0
    for mn,s in sorted(ms1,reverse=True):
        if cnt+mn<0:
            print("No")
            exit()
        cnt+=s

    cnt2=0
    for mn,s in sorted(ms2,reverse=True):
        if cnt2+mn<0:
            print("No")
            exit()
        cnt2+=s

    if cnt==cnt2:print("Yes")
    else:print("No")

main()