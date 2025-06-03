(r, c) = map(int, input().split())
a = [[v for v in list(map(int, input().split()))] for r in range(r)]
add_c = [sum(l) for l in a]
for i in range(r):
    a[i].append(add_c[i])
add_r = [sum([a[i][j] for i in range(r)]) for j in range(c + 1)]
a.append(add_r)
for i in range(r + 1):
    print(' '.join(map(str, a[i])))