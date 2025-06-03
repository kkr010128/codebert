from collections import Counter
import math

def combinations_count(n):
    return (n * (n - 1)) // 2

N = int(input())
A = list(map(int, input().split()))

combs = {}
dic = Counter(A)
for k, v in dic.items():
    combs[k] = combinations_count(v)
ans = sum(combs.values())

for i in range(N):
    a = A[i]
    ans_i = ans
    if combs[a] < 2:
        ans_i -= combs[a]
        print(ans_i)
    else:
        ans_i -= dic[a] - 1
        print(ans_i)
