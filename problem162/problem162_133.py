import math

nums = [int(e) for e in input().split()]
n = nums[0]
m = nums[1]

x = -1
y = -1

ms = []

if n%2 == 0:
    x = 1
    y = n
    count = True

    while x < y:
        if y-x <= n/2 and count:
            y -= 1
            count = False
        ms += [[x,y]]
        x += 1
        y -= 1


else:
    x = 1
    y = n
    while x < y:
        ms += [[x, y]]
        x += 1
        y -= 1


# print(ms)

for i in range(m):
    print(str(ms[i][0]) + " " + str(ms[i][1]))
