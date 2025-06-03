N=int(input())
A=list(map(int,input().split()))

if A[0]:
    if N==0 and A[0]==1:
        print(1)
    else:
        print(-1)
    exit()

B=[0 for _ in range(N)]

B.append(A[-1])
for i in range(N)[::-1]:
    B[i]=B[i+1]+A[i]

r=1
ans=1
for i in range(1,N+1):
    t=min(r*2,B[i])
    ans+=t
    r=t-A[i]
    if r<0:
        print(-1)
        exit()

print(ans)