import itertools

N = int(input())
dots = [tuple(map(int, input().split())) for _ in range(N)]
total_distance = 0
total_count = 0

for route in itertools.permutations(dots):
    for i in range(len(route)-1):
        x1, y1 = route[i]
        x2, y2 = route[i+1]

        total_distance += ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    total_count += 1

ans = total_distance / total_count
print(ans)


