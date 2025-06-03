import sys
import math
def IL(): return map(int,sys.stdin.readline().rstrip().split())

def Main():
    a,b,n = IL()
    x = min(b-1,n)
    print(math.floor(a*x/b)-a*math.floor(x/b))
    return

if __name__=='__main__':
    Main()