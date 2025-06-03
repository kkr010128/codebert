import math

n = int(input())
x = []
x.extend(list(map(int, input().split())))
y = []
y.extend(list(map(int, input().split())))

i = 0
sum = 0
for i in range(n):
    sum += abs(x[i] - y[i])

print(sum)

sum = 0
for i in range(n):
    sum += (x[i] - y[i]) ** 2

print(math.sqrt(sum))

sum = 0
for i in range(n):
    sum += abs(x[i] - y[i]) ** 3

print(sum ** (1/3))

check = 0
for i in range(n):
    if check < abs(x[i] - y[i]):
        check = abs(x[i] - y[i])

print(check)

