import sys
input = sys.stdin.readline
N, D = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(N)]

D_2 =pow(D, 2)
count = 0
for i in range(N):
    a = pow(points[i][0], 2) + pow(points[i][1], 2)
    if D_2 >= a:
        count +=1

print(count)
