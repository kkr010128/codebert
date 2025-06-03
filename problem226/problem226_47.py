import sys
input = sys.stdin.readline
from collections import *

H, N = map(int, input().split())
A = list(map(int, input().split()))

if H-sum(A)<=0:
    print('Yes')
else:
    print('No')