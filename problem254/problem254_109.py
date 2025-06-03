import sys
import  math
import fractions
from collections import defaultdict
stdin = sys.stdin
     
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))

A=int(input())
B=int(input())
A2=min(A,B)
B2=max(A,B)
if(A2==1 and B2==2):
    print(3)
    sys.exit(0)

if(A2==2 and B2==3):
    print(1)
    sys.exit(0)

if(A2==1 and B2==3):
    print(2)
    sys.exit(0)
