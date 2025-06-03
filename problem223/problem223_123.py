N,K=map(int,input().split())
P=list(map(int,input().split()))
from itertools import accumulate
acc=[0]+list(accumulate(P))
print((max(b-a for a,b in zip(acc,acc[K:]))+K)/2)