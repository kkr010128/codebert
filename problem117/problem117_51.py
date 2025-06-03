import itertools
N,M,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A_=[0]+list(itertools.accumulate(A))
B_=[0]+list(itertools.accumulate(B))

ans=0
j=M
for i in range(N+1):
    a=A_[i]
    K_a=K-a
    while (j>=0 and B_[j]>K_a):
        j-=1
    if a+B_[j]<=K:
        ans=max(ans,i+j)
print(ans)
