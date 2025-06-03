import itertools
import math

N = int(input())
xy = []
for _ in range(N):
    xi, yi = map(int, input().split())
    xy.append([xi, yi])

# print(xy)

sum_dist = 0

# 第二引数を指定しなければ全ての要素の順列を返す
for perm in itertools.permutations(range(N)):
    dist = 0
    for i in range(1, N):
        dist += math.sqrt((xy[perm[i]][0] - xy[perm[i - 1]][0]) **
                          2 + (xy[perm[i]][1] - xy[perm[i - 1]][1])**2)
    # print(sum_dist)
    sum_dist += dist

ans = sum_dist / math.factorial(N)
print(ans)
