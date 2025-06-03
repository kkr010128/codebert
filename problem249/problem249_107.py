A, B, K = [int(x) for x in input().split()]

if A >= K:
    print("{} {}".format(A-K, B))
    exit()

K -= A
A = 0

if B >= K:
    print("{} {}".format(A, B-K))
    exit()

print("{} {}".format(0, 0))
