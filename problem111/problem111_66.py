import math
N=int(input())
A=[int(x) for x in input().split()]
ans=0
A=sorted(A)
ans+=A[N-1]
for i in range(1,N-1):
    ans+=A[N-1-math.ceil(i/2)]
print(ans)