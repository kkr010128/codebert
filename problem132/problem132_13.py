n,k=map(int,input().split())
A=list(map(int,input().split()))
C=[n for _ in range(n)]

for loop in range(k):
    B=[0 for _ in range(n)]
    for i in range(n):
        l,r=max(0,i-A[i]),i+A[i]+1
        B[l] +=1
        if r<n:B[r] -=1
    for i in range(n-1):
        B[i+1]=B[i]+B[i+1]
    A=B
    if A==C:break
print(*A)