import itertools
import math

n = int(input())

#座標のリスト
xy_list = []
for i in range(n) :
    xy_list.append(list(map(int, input().split())))

#順列を生成
per_list = []
for j in itertools.permutations([x for x in range(n)]) :
    per_list.append(j)

#順列に従って距離を加算
d = 0
for k in per_list :
    for l in range(n - 1) :
        d += math.sqrt((xy_list[k[l + 1]][0] - xy_list[k[l]][0]) ** 2 + (xy_list[k[l + 1]][1] - xy_list[k[l]][1]) ** 2)
        
print(d/(len(per_list)))