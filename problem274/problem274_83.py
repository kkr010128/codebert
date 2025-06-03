import sys
sys.setrecursionlimit(10000000)
import math
import bisect
from collections import deque
def input():
    return sys.stdin.readline()[:-1]
    
n,m = map(int,input().split())
s = input()
lis = []
now = len(s)-1
ju = 0
ju2 = 0
while now>0:
    ju = 0
    if ju2==1:
        break
    for i in range(m,0,-1):
        if now-i<0:
            continue
        if now-i ==0:
            lis.append(i)
            ju = 1
            now = 0
            break
        if s[now-i]=="0":
            now = now-i
            lis.append(i)
            ju = 1
            break
        if i==1 and ju==0:
            ju2 = 1
            break
if ju2==0:
    lis.reverse()
    print(*lis)
else:
    print(-1)
