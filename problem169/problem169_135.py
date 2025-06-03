import numpy as np

# N: 会社員の人数
# 自分より番号が小さい人が直属の上司
N = int(input())
# A_i は社員番号iの直属の上司の社員番号
A = list(map(int, input().split()))

ans = np.zeros(N)

for i in range(N-1):
    ans[A[i]-1] += 1

for i in range(len(ans)):
    ans_str = int(ans[i])
    print(ans_str)
