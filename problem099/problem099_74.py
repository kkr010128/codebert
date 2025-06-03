import math
N, K = map(int, input().split())
A = [int(x) for x in input().split()]

left, right = 0, max(A)
while right - left > 1:
    mid = (left + right) // 2
    res = 0
    for i in range(N):
        res = res + math.ceil(A[i]/mid) - 1
    if res <= K:
        right = mid
    else:
        left = mid
print(right)