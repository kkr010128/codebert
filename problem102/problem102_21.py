N,K=map(int,input().split())
A=list(map(int,input().split()))
hyoutei=[0]*(N+1)
for i in range(K,N):#K+1-N
    if A[i]/A[i-K]>1:
        print("Yes")
    else:
        print("No")
