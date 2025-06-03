import math
from functools import reduce
INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))

def do():
    k=INT()
    ans=0
    for i in range(1,k+1):
        for j in range(1,k+1):
            for h in range(1,k+1):
                ans+=math.gcd(math.gcd(i,j),h)
                #print(ans,i,j,h)
    print(ans)
if __name__ == '__main__':
    do()