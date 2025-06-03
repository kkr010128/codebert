import math
N = int(input())
#https://qiita.com/jamjamjam888/items/e066b8c7bc85487c0785
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
l = 0

for j in range(N):
    for k in range(N):
        if j >= k:
            continue
        l += math.sqrt((x[j] - x[k])**2 + (y[j] - y[k]) ** 2)

print(l * 2/N)