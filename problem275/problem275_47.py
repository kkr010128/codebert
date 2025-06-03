X, Y = list(map(int, input().split()))
pX = [0 for _ in range(206)]
pX[1] = 300000
pX[2] = 200000
pX[3] = 100000

point = pX[X] + pX[Y]
if X == 1 and Y == 1:
    point += 400000

print(point)