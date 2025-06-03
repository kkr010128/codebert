A, B, C, K = map(int, input().split())

if A >= K:
    print(K)
else:
    K = K - A
    if B >= K:
        print(A)
    else:
        K = K - B
        print(A - K)