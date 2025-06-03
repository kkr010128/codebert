N=int(input())
A=list(map(int,input().split()))

L={}
R={}
ans=0
for i in range(N):
    if i+A[i] in L:
        L[i+A[i]]+=1
    else:
        L[i+A[i]]=1
    if A[i]<=i:
        if i-A[i] in R:
            R[i-A[i]]+=1
        else:
            R[i-A[i]]=1
for r in R:
    if r in L:
        ans+=L[r]*R[r]
print(ans)