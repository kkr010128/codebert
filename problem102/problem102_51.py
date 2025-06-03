N, K = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if i < K:
        continue

    if A[i-K] < A[i]:
        print('Yes')
    else:
        print('No')
