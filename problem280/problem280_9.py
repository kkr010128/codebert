N = int(input())
town = [list(map(int, input().split())) for _ in range(N)]

s = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        s += ((town[i][0] - town[j][0])**2 + (town[i][1] - town[j][1])**2)**0.5

print(s / N)