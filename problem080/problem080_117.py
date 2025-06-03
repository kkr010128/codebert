z = []
w = []

for _ in range(int(input())):
    x, y = map(int, input().split())
    z.append(x + y)
    w.append(x - y)


z_max = max(z)
z_min = min(z)
w_max = max(w)
w_min = min(w)

print(max([abs(z_max - z_min), abs(w_max - w_min)]))