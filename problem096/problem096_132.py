n, d = map(int, input().split())
points = [list(map(int, input().split(' '))) for i in range(n)]
cnt = 0

for i in range(n):
    square_distance = points[i][0]**2 + points[i][1]**2
    if square_distance <= d**2:
        cnt += 1
print(cnt)