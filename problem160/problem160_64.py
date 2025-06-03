# ABC165 C
from itertools import combinations as com

N,M,Q=map(int,input().split())
query=[tuple(map(int,input().split())) for _ in [0]*Q]

res=0
for p in com(list(range(N+M-1)),M-1):
    m=1
    A=[]
    for i in range(N+M-1):
        if i in p:
            m+=1
        else:
            A.append(m)
    tmpres=0
    for a,b,c,d in query:
        if A[b-1]-A[a-1]==c:
            tmpres+=d
#     print(p,A,tmpres)
    res=max(tmpres,res)
print(res)