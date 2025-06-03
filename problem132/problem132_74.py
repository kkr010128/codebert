n, k = map(int, input().split())

aa = list(map(int, input().split()))

from itertools import accumulate

aa

for _ in range(k):
    d = [0] * n

    for i, a in enumerate(aa):
        d[max(i-a, 0)] += 1
        end = i+1+a
        if end < n:
            d[end] -= 1

    d = list(accumulate(d))
    if aa == d:
        break
    aa = d


print(' '.join(str(a) for a in aa))