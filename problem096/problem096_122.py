import math
n,d = map(int,input().split())
point_list = [0,0]*n
for i in range(n):
    point = list(map(int,input().split()))
    point_list[i]=point
count = 0

for j in range(n):
    distance = math.sqrt(point_list[j][0]**2 + point_list[j][1]**2)
    if distance <= d:
        count += 1

print(count)