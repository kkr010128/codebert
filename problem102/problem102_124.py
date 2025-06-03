N,K=map(int,input().split())
A=list(map(int,input().split()))

for i in range(K-1,N-1):
    a=A[i-K+1]
    b=A[i+1]
    if(a<b):
        print('Yes')
    else:
        print('No')