a, b, c, d = map(int, input().split())
e = []
for i in [a, b]:
    for j in [c, d]:
        e += [i * j]

print(max(e))