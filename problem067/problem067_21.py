def judge():
    if t > h:
        point["t"] += 3
    elif t < h:
        point["h"] += 3
    else:
        point["t"] += 1; point["h"] += 1

n = int(input())
point = {"t": 0, "h": 0}
for i in range(n):
    t, h = input().split()
    judge()
print(point["t"], point["h"])

