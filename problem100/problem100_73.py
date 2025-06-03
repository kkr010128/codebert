# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

X=int(input())
if X>=1800:
    print(1)
elif X>=1600:
    print(2)
elif X>=1400:
    print(3)
elif X>=1200:
    print(4)
elif X>=1000:
    print(5)
elif X>=800:
    print(6)
elif X>=600:
    print(7)
elif X>=400:
    print(8)