import sys
from collections import Counter
from itertools import accumulate
read = sys.stdin.read

N, K, *A = map(int, read().split())
a = list(accumulate([0] + A))
a = [(a[i] - i) % K for i in range(N + 1)]

answer = 0
if N < K:
    for i in Counter(a).values():
        answer += i * (i - 1) // 2
else:
    dic = Counter(a[:K])
    for i in dic.values():
        answer += i * (i - 1) // 2
    here = K
    for i, x in enumerate(a[K:]):
        dic[a[i]] -= 1
        answer += dic[x]
        dic[x] += 1

print(answer)