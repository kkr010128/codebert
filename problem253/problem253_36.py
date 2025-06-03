N, A, B = [int(x) for x in input().split()]

if (B-A) % 2 == 0:
    print((B-A) // 2)
else:
    print(min(A-1, N-B) + 1 + (B - A - 1) // 2)
