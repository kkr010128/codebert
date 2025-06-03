import math
x = int(input())

# -100 ~ 100 ^ 5
pow5 = {}
for i in range(-1000, 1001):
    pow5[i] = int(math.pow(i, 5))

for i in range(-1000, 1001):
    a = x + pow5[i]
    for j in range(-1000, 1001):
        if a == pow5[j]:
            print(j, i)
            exit()
