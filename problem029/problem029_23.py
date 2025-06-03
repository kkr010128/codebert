import math

point =list(map(float, input().split()))
p1 = point[0]
p2 = point[1]
p3 = point[2]
p4 = point[3]

l = math.sqrt((p3 - p1)**2 + (p4 - p2)**2)

print(l)