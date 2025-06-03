"""from collections import *
from itertools import *
from bisect import *
from heapq import *

import math
from fractions import gcd"""

T1,T2=map(int,input().split())
A1,A2=map(int,input().split())
B1,B2=map(int,input().split())

A1*=T1
A2*=T2
B1*=T1
B2*=T2

if A1+A2==B1+B2:
    print("infinity")
else:
    if A1+A2<B1+B2:
        A1,B1=B1,A1
        A2,B2=B2,A2
    if A1>B1:
        print(0)
    else:
        print(((B1-A1)//(A1+A2-(B1+B2)))*2 +1-(((B1-A1)%(A1+A2-(B1+B2)))==0)*1)
