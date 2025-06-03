#C
N=int(input())
A=[int(x) for x in input().split()]

P=[0 for i in range(N+1)]
P[N]=[A[N],A[N]]
for i in range(N-1,-1,-1):
    MIN,MAX=P[i+1]
    mi=int(A[i]+(MIN+MIN%2)/2)
    ma=A[i]+MAX
    P[i]=[mi,ma]
    
    
if P[0][0]==1:
    Q=[0 for i in range(N+1)]
    Q[0]=1
    cnt=1
    for i in range(N):
        Q[i+1]=min((Q[i]-A[i])*2,P[i+1][1])
        cnt+=Q[i+1]
    print(cnt)
else:
    print("-1")