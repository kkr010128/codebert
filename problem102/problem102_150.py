N, K = map(int, input().split())
A = [int(i) for i in input().split()]
i_list = [0] * N

for i in range(K, N):
    if A[i-K] < A[i]:
        print('Yes')
    else:
        print('No')