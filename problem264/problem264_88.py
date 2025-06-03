import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    M,D=map(int,input().split())
    N,E=map(int,input().split())

    print(1 if M!=N else 0)

resolve()