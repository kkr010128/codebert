import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a=int(input())
    print(a+a**2+a**3)
resolve()