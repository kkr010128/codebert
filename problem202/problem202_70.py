# ABC158 B - Count Balls

M,A,B = map(int,input().split())
import math
C = math.floor(M/(A+B))
N = M%(A+B)
E = C*A

if N >= A:
    E+=A
else:
    E+=N
print(E)
        
        
