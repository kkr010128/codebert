r, c = map(int, input().split())
lis = [[] for a in range(r+1)]
for x in range(r):
    lis[x] = list(map(int, input().split()))
    lis[x].append(sum(lis[x]))
lis[r] = [0 for a in range(c+1)]
for y in range(c+1):
    for z in range(r):
        lis[r][y] += lis[z][y]
for x in lis:
    for z,y in enumerate(x):
        if z == c:
            print(y)
        else:
            print(y, end = " ")


