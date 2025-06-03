import itertools
import math
N = int(input())
XY = [list(map(int, input().split())) for i in range(N)]
n = [i for i in range(N)]

dist = 0
cnt = 0
for target_list in list(itertools.permutations(n)):
    for i in range(len(target_list)):
        if i == 0:
            continue
        dist += math.sqrt((XY[target_list[i]][0] - XY[target_list[i-1]][0]) ** 2 + (XY[target_list[i]][1] - XY[target_list[i-1]][1]) ** 2)
    cnt += 1
print(dist / cnt)