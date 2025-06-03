A, B, C, K = map(int, input().split())
D = A + B
if D >= K:
    print(min(K,A))
else:
    K -= D
    print(A-K)
