import itertools
import functools
import math
from collections import Counter

def CHK():
    X,Y,A,B,C=map(int,input().split())
    p=sorted(list(map(int,input().split())),reverse=True)
    q=sorted(list(map(int,input().split())),reverse=True)
    r=sorted(list(map(int,input().split())),reverse=True)

    apples = sorted(p[:X] + q[:Y] + r, reverse=True)

    ans = sum(apples[:X+Y])
    print(ans)

CHK()