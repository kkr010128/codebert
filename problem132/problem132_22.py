import sys
import  math
import fractions
from collections import defaultdict
stdin = sys.stdin
     
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))

N,K=nm()
A=nl()

imos_l=[0]*(N+1)

for i in range(K):    
    imos_l=[0]*(N+1)
    for j in range(len(A)): 
        imos_l[max(j-A[j],0)]+=1
        imos_l[min(j+A[j]+1,N)]-=1
    for j in range(len(imos_l)-1):
        imos_l[j+1]=imos_l[j]+imos_l[j+1]
    for j in range(len(A)):
        A[j]=imos_l[j]
    flag=True
    for j in range(len(A)):
        if(A[j]<N):
            flag=False
    if(flag):
        print(*A)
        sys.exit(0)

print(*A)
            
        

