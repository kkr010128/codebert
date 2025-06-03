from itertools import permutations
from math import sqrt, pow, factorial

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

def calc(a,b):
    [x1, y1] = a
    [x2, y2] = b
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

sum = 0
for i in permutations(range(n)):
    distance = 0
    for j in range(1, n):
        distance = calc(xy[i[j]], xy[i[j-1]])
        sum += distance
print(sum/factorial(n))




