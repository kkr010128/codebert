A, B, K = [int(x) for x in input().split()]
if K <= A:
    print(A - K, B)
else:
    print(0, max(0, A + B - K))