N,K = map(int, input().split())
A = [0] + list(map(int, input().split()))

for i in range(K+1, N+1):
    if A[i-K] >= A[i]:
        print('No')
    else:
        print('Yes')