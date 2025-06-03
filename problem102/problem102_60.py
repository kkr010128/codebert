N,K=map(int,input().split())
A=list(map(int,input().split()))
s_p=sum(A[:K])

for i in range(N-K):
    s=s_p+A[i+K]-A[i]
    if s_p < s:
       print('Yes')
    else:
        print('No')