import math
import sys
import bisect
import array

m=10**9 + 7 
sys.setrecursionlimit(1000010)
(N,K) = map(int,input().split())
A = list( map(int,input().split())) 
# print(N,K,A)
B = list( map(lambda x: x % K, A))
C = [0]
x = 0
i = 0 
for b in B:
    x = (x + b ) % K 
    C.append((x-i-1) % K) 
    i += 1 
    
# print(B,C)

E={}


ans=0
for i in range(N+1):
    if C[i] in E:
        ans += E[C[i]]
        E[C[i]] = E[C[i]] + 1
    else:
        E[C[i]] = 1
    if i >= K-1:
        E[C[i-K+1]] = E[C[i-K+1]] - 1
        if E[C[i-K+1]] == 0:
             E.pop(C[i-K+1])

print(ans)
exit(0)