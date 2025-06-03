import math

nd = list(map(int,input().split(" ")))
n = nd[0]
d = nd[1]
cnt = 0


xy=[]
for i in range(n):
    xy.append(list(map(int,input().split(" "))))
    result = math.sqrt((xy[i][0]**2)+(xy[i][1]**2))
    if result <= d:
        cnt += 1

print(cnt)