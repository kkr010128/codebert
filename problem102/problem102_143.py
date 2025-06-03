N, K = map(int, input().split())
A = list(map(int, input().split()))

for idx, a in enumerate(A):
    if idx < K:
        continue
    else:
        if a <= A[idx - K]:
            print('No')
        else:
            print('Yes')