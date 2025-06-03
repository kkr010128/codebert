import sys
from collections import defaultdict
N,S=map(int, sys.stdin.readline().split())
A=map(int, sys.stdin.readline().split())

mod=998244353
cur=defaultdict(lambda: 0)
new=defaultdict(lambda: 0)
cur[0]=1

for a in A:
    for i in cur.keys():
        if i+a<=S:
            new[i+a]+=cur[i]
            new[i+a]%=mod
        new[i]+=cur[i]*2
        new[i]%=mod
    cur=new
    new=defaultdict(lambda: 0)

print cur[S]
