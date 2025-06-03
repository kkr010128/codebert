import math
X = int(input())

count = 0
s = 100
while s < X:
    #s = math.floor(s*1.01)
    s += s//100
    count += 1
print(count)