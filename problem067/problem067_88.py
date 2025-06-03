import sys
n = int(sys.stdin.readline())
points = [0, 0]
for i in range(n):
    (taro, hanako) = sys.stdin.readline().split()
    if taro < hanako:
        points[1] += 3
    elif taro > hanako:
        points[0] += 3
    else:
        points[0] += 1
        points[1] += 1
print(points[0], points[1])