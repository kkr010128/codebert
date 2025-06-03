def update(A,N):
    B=[0 for i in range(N+1)]

    for i in range(N):
        l = max(0,i-A[i])
        r = min(N,i+A[i]+1)
        B[l]+=1
        B[r]-=1
    x = A[0] == B[0]
    A[0]=B[0]
    for i in range(1,N):
        B[i]+=B[i-1]
        x = x and A[i] == B[i]
        A[i]=B[i]
    return x

def resolve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    for i in range(M):
        x=update(A,N)
        if x:
            break
    print(" ".join(map(str,A)))
resolve()
