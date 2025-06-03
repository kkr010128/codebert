n = int(input())
robot = [0]*n
for i in range(n):
    x,l = map(int,input().split())
    robot[i] = (x+l, x-l)
robot.sort()

#print(robot)

ans = 1
right = robot[0][0]
for i in range(1,n):
    if right <= robot[i][1]:
        right = robot[i][0]
        ans += 1
print(ans)