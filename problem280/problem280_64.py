import math
N = int(input())
town = []
for i in range(N):
    x, y = map(int, input().split())
    town.append((x, y))
    

def dfs(current, dist, already):
    if len(already) == N:
        return dist
    d = 0
    for i in range(N):
        if i in already:
            continue
        d += dfs(i, dist + math.sqrt((town[current][0] - town[i][0]) ** 2 + (town[current][1] - town[i][1]) ** 2), already | set([i]))
    return d
answer = 0
for i in range(N):
    answer += dfs(i, 0, set([i]))
print(answer / math.factorial(N))