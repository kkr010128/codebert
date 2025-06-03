N=int(input())
A=list(map(int,input().split()))
import itertools
ACU=itertools.accumulate(A)
B=list(ACU)
MAX=B[-1]
tmp=10**10
for i in B:
  tmp=min(tmp,abs(2*i-MAX))
print(tmp)