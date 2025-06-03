from itertools import accumulate
import bisect

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

SA = [0] + list(accumulate(A))
SB = [0] + list(accumulate(B))

max_count = 0
for i in range(N + 1):
    a_count = i
    b_count = bisect.bisect_right(SB, K - SA[a_count]) - 1
    if b_count >= 0:
        count = a_count + b_count
        if count > max_count:
            max_count = count
        
print(max_count)