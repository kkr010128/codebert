import math

N, M = map(int, input().split())
A_list = list(map(int, input().split()))

cnt = 0
A_sum = sum(A_list)

for i in range(N):
    if A_list[i] >= math.ceil(A_sum/4/M):
        cnt += 1
if cnt >= M:
    print("Yes")
else:
    print("No")
