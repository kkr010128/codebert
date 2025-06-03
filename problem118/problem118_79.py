import math
N = int(input())
cnt_list = [0] * N
for i in range(1, N + 1):
    for j in range(i, N + 1, i):
        cnt_list[j - 1] += 1
ans = 0
for h in range(1, N + 1):
    ans += h * cnt_list[h -1]
print(ans)