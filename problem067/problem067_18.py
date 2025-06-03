round = int(input())
points =[0, 0]
for r in range(round):
    taro, hanako = input().split(" ")
    if taro == hanako:
        points[0] += 1
        points[1] += 1
    elif taro > hanako:
        points[0] += 3
    elif taro < hanako:
        points[1] += 3

print(*points)