N = int(input())
robot = []
ans = 0
for i in range(N):
    x,l = map(int,input().split())
    robot.append([x+l,x-l])
robot.sort()

cur = -float('inf')

for i in range(N):
    if cur <= robot[i][1]:
        ans += 1
        cur = robot[i][0]

print(ans)