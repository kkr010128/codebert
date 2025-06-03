N = int(input())
A = list(map(int, input().split()))
m=1000
s=0
if A[0]<A[1]:
    s=int(1000/A[0])
    m=m-s*A[0]
for i in range(1,N-1,1):
    m=m+s*A[i]
    s=0
    if A[i+1]>A[i]:
        s=int(m/A[i])
        m=m-s*A[i]
m=m+max(A[N-1],A[N-2])*s
print(m)