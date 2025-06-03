import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n,r=map(int, input().split())
    if n>=10:
        print(r)
    else:
        print(r+100*(10-n))
resolve()