import math , sys, bisect

N , M , K = list( map( int , input().split() ))
A = list( map( int , input().split() ))
B = list( map( int , input().split() ))
if N > M:
    N , M = M , N
    A, B = B , A

Asum=[0]
Bsum=[]
if A[0] > K and B[0] > K:
    print(0)
    sys.exit()

for i in range(N):
    if i ==0:
        tot = A[i]
    else:
        tot += A[i]
    Asum.append(tot)

for i in range(M):
    if i ==0:
        tot = B[i]
    else:
        tot += B[i]
    Bsum.append(tot)

#ans=bisect.bisect(Bsum,K)
ans=0
for i in range(N+1):
    tot = Asum[i]
    if tot > K:
        print(ans)
        sys.exit()
    num = bisect.bisect(Bsum,K-tot)
    if i + num >ans:
        ans=i+num
print(ans)