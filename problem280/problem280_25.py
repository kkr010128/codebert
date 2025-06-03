import itertools
import math

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
numbers = list(range(1, n + 1))
diff = 0
count = 0
for pattern in itertools.permutations(numbers):
    count += 1
    for j in range(n - 1):
        points_index = pattern[j] - 1
        next_index = pattern[j + 1] - 1
        diff += math.sqrt((points[points_index][0] - points[next_index][0]) ** 2 + (points[points_index][1] - points[next_index][1]) ** 2)

print(diff / count)
