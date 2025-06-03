A, B, K = map(int, input().split())

if A + B == 0:
    print(0, 0)
elif A - K >= 0:
    print(A-K, B)
elif A + B- K >= 0:
    print(0, A+B-K)
else:
    print(0, 0)