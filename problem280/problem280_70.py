import itertools

n = int(input())
twn = [list(map(int, input().split())) for _ in range(n)]
twnst = list(itertools.permutations(twn))
dstttl = 0
for i in twnst:
    for j in range(0, len(i) - 1):
        dstttl += (abs(i[j][0] - i[j+1][0])**2 + abs(i[j][1] - i[j+1][1])**2)**0.5
print(dstttl / len(twnst))