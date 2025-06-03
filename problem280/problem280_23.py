from itertools import permutations

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

sum = 0
cnt = 0
for i in permutations(xy):
    for j in range(n - 1):
        sum += ((i[j][0] - i[j + 1][0]) ** 2 + (i[j][1] - i[j + 1][1]) ** 2) ** 0.5
    cnt += 1
print(sum / cnt)