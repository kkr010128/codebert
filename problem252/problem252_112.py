from sys import stdin
f_i = stdin

N, M = map(int, f_i.readline().split())
A = list(map(int, f_i.readline().split()))

A.sort()

from bisect import bisect_left

def shake_count(power):
    return N ** 2 - sum(bisect_left(A, power - left_hand) for left_hand in A)

lower = A[0] * 2 - 1
upper = A[-1] * 2 + 1
while lower + 1 < upper:
    mid = (lower + upper) // 2
    if shake_count(mid) >= M:
        lower = mid
    else:
        upper = mid

X = tuple(bisect_left(A, upper - left_hand) for left_hand in A)

from itertools import accumulate
acc = tuple(accumulate([0] + A))

s = acc[-1]
ans = sum(s - acc[x] for x in X) + sum(a * (N - x) for a, x in zip(A, X))

rest_shake_count = M - (N ** 2 - sum(X))
ans += lower * rest_shake_count

print(ans)