import bisect
N, M, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
a_sum = []
b_sum = []
sm = 0
for a in A:
    sm += a
    if sm > K:
        break
    a_sum.append(sm)
sm = 0
for b in B:
    sm += b
    if sm > K:
        break
    b_sum.append(sm)
index_max = 0
# a_size = len(a_sum)
# for i in range(a_size):
while a_sum:
    a_size = len(a_sum)
    b_index = bisect.bisect_right(b_sum, K - a_sum.pop())
    index_max = max(index_max, a_size + b_index)
    # print(a_size, b_index)
b_index = bisect.bisect_right(b_sum, K)
index_max = max(index_max, b_index)
print(index_max)