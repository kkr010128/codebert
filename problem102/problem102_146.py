N, K, *A = map(int, open(0).read().split())

for a, b in zip(A[K:], A):
    if a > b:
        print("Yes")
    else:
        print("No")