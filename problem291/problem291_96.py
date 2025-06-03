import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b= map(int,input().split())
    print(0 if a-b*2<0 else a-b*2)
    
    
resolve()