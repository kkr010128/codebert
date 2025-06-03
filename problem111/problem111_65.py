import math

n = int(input())
values = list(map(int, input().split(' ')))

values.sort(reverse=True)
sum = 0

for i in range(1, n):
    sum += values[math.floor(i/2)]

print(sum)