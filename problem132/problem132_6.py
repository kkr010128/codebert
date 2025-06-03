N,K=map(int,input().split())
A=[0]+list(map(int,input().split()))+[0]
p=50

if K<=p:    
    for i in range(K):
        B=[0]+[0]*N+[0]
        for j in range(1,N+1):
            left  = max(0,j-A[j])
            right = min(N+1,j+A[j]+1)
            B[left]  += 1
            B[right] -= 1
        A[0]=B[0]
        for k in range(1,N+1):
            A[k]=A[k-1]+B[k]
else:
    A=[N]*(N+2)
print(*A[1:N+1])