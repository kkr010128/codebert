import collections, copy

h, w = map(int, input().split())
maze = []
maze.append("#" * (w + 2))
for i in range(h):
    maze.append("#" + input() + "#")
maze.append("#" * (w + 2))
dis = []
for i in range(h + 2):
    temp = [-1] * (w + 2)
    dis.append(temp)

def search(x, y):
    dis2 = copy.deepcopy(dis)
    move = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    queue = collections.deque([[x, y]])
    dis2[x][y] = 0
    while queue:
        test = queue.popleft()
        for i in move:
            place = [test[0] + i[0], test[1] + i[1]]
            if maze[place[0]][place[1]] == ".":
                if dis2[place[0]][place[1]] == -1:
                    dis2[place[0]][place[1]] = dis2[test[0]][test[1]] + 1
                    queue.append(place)
    return max([max([dis2[i][j] for j in range(w + 2)]) for i in range(h + 2)])

ans = 0
for i in range(h):
    for j in range(w):
        if maze[i + 1][j + 1] == ".":
            dist = search(i + 1, j + 1)
            ans = max(ans, dist)
print(ans)