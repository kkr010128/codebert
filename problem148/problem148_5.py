A, B, C, K = map(int, input().split())
if (K - A) <= 0:
    print(K)
else:
    if (K - A - B) <= 0:
        print(A)
    else:
        c = (K - A - B)
        print(A - c)
