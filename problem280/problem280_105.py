from itertools import permutations

def distance(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

d = 0
cnt = 0
for per in permutations(list(range(n)), n):
    cnt += 1
    for i in range(n-1):
        a = xy[per[i]]
        b = xy[per[i+1]]
        d += distance(a, b)

print(d/cnt)