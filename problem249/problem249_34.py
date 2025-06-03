A, B, K = list(map(int, input().split()))

A_res = max(0, A - K)
B_res = max(0, B - K + A - A_res)

print("{} {}".format(A_res, B_res))