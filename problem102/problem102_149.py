a = list(map(int,input().split()))
A = list(map(int,input().split()))
N = a[0]
K = a[1]

for i in range(K,N):
    if A[i] > A[i-K]:
        print('Yes')
    else:
        print('No')