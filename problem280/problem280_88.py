import itertools

N = int(input())
cities = [tuple(map(int, input().split())) for _ in range(N)]

distance = 0
for c in itertools.combinations(range(N), 2):
    c1, c2 = c
    distance += ((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2) **0.5

answer = 2 * distance / N

print(answer)
