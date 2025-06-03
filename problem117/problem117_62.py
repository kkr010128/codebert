import bisect
from itertools import accumulate

N, M, K = map(int, input().split())
A = map(int, input().split())
B = map(int, input().split())

A_cumsum = list(accumulate(A))
B_cumsum = list(accumulate(B))

max_books = 0
for a, A_sum in enumerate([0] + A_cumsum):
    if A_sum > K:
        break
    else:
        b = bisect.bisect(B_cumsum, K - A_sum)
        max_books = max(a + b, max_books)

print(max_books)
