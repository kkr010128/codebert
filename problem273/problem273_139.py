import sys
from itertools import accumulate
from collections import defaultdict
input = sys.stdin.readline
N,K=map(int,input().split());A=list(map(int,input().split()))
S_=list(map(lambda t: (t[1]-t[0])%K,enumerate(accumulate([0]+A))))
count=0
C=defaultdict(int)
for t in range(1,N+1):
  C[S_[t-1]]+=1
  if t-K>=0:
    C[S_[t-K]]-=1
  count+=C[S_[t]]
print(count)
