N,K = map(int,input().split())
A = list(map(int,input().split()))
A.insert(0,0)
for i in range(K+1,N+1):
    if A[i]>A[i-K]:
        print("Yes")
    else:
        print("No")