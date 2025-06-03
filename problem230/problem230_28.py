import bisect
import math

N, D, A = map(int, input().split())

XH_array = [list(map(int, input().split())) for _ in range(N)]

XH_array = sorted(XH_array, key=lambda x: x[0])

X_array = [xh[0] for xh in XH_array]

# print(X_array)

ans = 0
bomb_count = [0] * N
now_bomb = 0

for i, xh in enumerate(XH_array):
    # print(now_bomb, bomb_count)
    x, h = xh
    remain = h - A * now_bomb
    if remain <= 0:
        now_bomb += bomb_count[i]
        continue
    bomb_add = math.ceil(remain / A)
    ans += bomb_add
    bomb_count[i] += bomb_add
    bomb_end = bisect.bisect_right(X_array, x + 2 * D)
    bomb_count[bomb_end - 1] -= bomb_add
    now_bomb += bomb_count[i]


print(ans)
