import sys
from decimal import Decimal
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b,c=map(int, input().split())
    if Decimal(a).sqrt()+Decimal(b).sqrt()<Decimal(c).sqrt():
        print('Yes')
    else:
        print('No')
resolve()