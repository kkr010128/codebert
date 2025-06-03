n, m = map(int,input().split())
h = list(map(int,input().split()))
neighbor = [[0] for _ in range(n)]
good = 0

for i in range(m):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    neighbor[a].append(h[b])
    neighbor[b].append(h[a])

for i in range(n):
    my_height = h[i]
    neighbor_height = neighbor[i]
    if all(my_height > x for x in neighbor_height):
        good += 1

print(good)