# C
import copy
import itertools

n, k = map(int, input().split())
a_list = [int(x) for x in input().split()]

for j in range(k):
    b_list = [0]*n
#     print("a:",*a_list)
    for i in range(n):
        l = max(0, i-a_list[i])
        r = min(n-1, i+a_list[i])
        b_list[l] += 1
        if r+1 < n:
            b_list[r+1] -= 1
#     print("b:",*b_list)
    cumsum = list(itertools.accumulate(b_list))
    if cumsum == [n]*n:
        break
    a_list = cumsum
print(*cumsum)