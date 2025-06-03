r, c = map(int, input().split())
data = [list(map(int, input().split())) for i in range(r)]
for i in range(r):
    data[i].append(sum(data[i]))
data.append([sum(data[j][i] for j in range(r)) for i in range(c + 1)])
for i in range(r + 1):
    for j in range(c + 1):
        print(data[i][j], end='')
        if j != c:
            print(' ', end='')
    print('')