a, b = map(int, input().split())
sheet = [list(map(int, input().split())) for i in range(a)]
for row in sheet:
    print(' '.join(map(str, row + [sum(row)])))
lastrow = [sum([j[i] for j in sheet]) for i in range(b)]
print(' '.join(map(str, lastrow + [sum(lastrow)])))
