#E
from bisect import bisect_left
from itertools import accumulate

N,M=map(int,input().split())
A=list(map(int,input().split()))
A=sorted(A)
A_r=list(reversed(A))
B=[0]+list(accumulate(A_r))

def f(x):
    count=0
    for i in A:
        idx=bisect_left(A,x-i)
        count+=N-idx
    if count>=M:
        return True
    else:
        return False
    
MIN=0
MAX=2*10**5+1
while MAX-MIN>1:
    MID=(MIN+MAX)//2
    if f(MID):
        MIN=MID
    else:
        MAX=MID

ans=0
count=0
for i in A_r:
    idx=bisect_left(A,MIN-i)
    ans+=i*(N-idx)+B[N-idx]
    count+=N-idx
print(ans-(count-M)*MIN)