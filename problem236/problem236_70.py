# import string
import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    h=int(input())
    w=int(input())
    n=int(input())

    v=max(h,w)
    cnt=0
    while n>0:
        n-=v
        cnt+=1
    print(cnt)

resolve()