N=int(input())
A=list(map(int,input().split()))
D={}
for i in range(N):
    if not(A[i] in D):
        D[A[i]]=0
    D[A[i]]+=1
ans=0
for i in D:
    ans+=(D[i]*(D[i]-1))//2
for k in range(N):
    print(ans-D[A[k]]+1)

