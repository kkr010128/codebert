from itertools import accumulate


N, *A = map(int, open(0).read().split())
A_acc = list(accumulate(A, initial=0))
min_diff = float("inf")
for i in range(1, N):
    left, right = A_acc[i], A_acc[N] - A_acc[i]
    min_diff = min(min_diff, abs(right - left))
print(min_diff)
