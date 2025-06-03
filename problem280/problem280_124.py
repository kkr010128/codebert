import math
import itertools

# 与えられた数値の桁数と桁値の総和を計算する.
def calc_digit_sum(num):
    digits = sums = 0
    while num > 0:
        digits += 1
        sums += num % 10
        num //= 10
    return digits, sums


n = int(input())
distances = []
for _ in range(n):
    points = list(map(int, input().split()))
    distances.append(points)

total = 0
routes = list(itertools.permutations(range(n), n))
for route in routes:
    distance = 0
    for index in range(len(route)-1):
        idx1 = route[index]
        idx2 = route[index+1]
        distance += math.sqrt((distances[idx1][0] - distances[idx2][0]) ** 2 + (distances[idx1][1] - distances[idx2][1]) ** 2)
    total += distance

print(total / len(routes))
