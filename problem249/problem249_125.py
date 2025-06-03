A, B, K = map(int, input().split())

if K <= A:
    print("{} {}".format(A - K, B))
else:
    K -= A
    print("{} {}".format(0, max(B - K, 0)))
