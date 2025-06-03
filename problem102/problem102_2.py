N, K, *A = [int(_) for _ in open(0).read().split()]
for a, b in zip(A, A[K:]):
    print('Yes' if a < b else 'No')
