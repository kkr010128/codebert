if __name__ == '__main__':
    n = int(input())
    graph = [[0 for i in range(n)] for _ in range(n)]
    frist = [0 for _ in range(n)]
    end = [0 for _ in range(n)]
    visit = [False for _ in range(n)]
    # get the group
    for i in range(n):
        datas = [int(num) for num in input().split(' ')]
        if datas[1] > 0:
            for j in datas[2:]:
                graph[datas[0] - 1][j - 1] = 1

    queue = [0]
    visit = [False for _ in range(n)]
    visit[0] = True
    depths = [0 for _ in range(n)]
    while len(queue) != 0:
        point = queue.pop(0)
        for i in range(n):
            if graph[point][i] == 1 and visit[i] is False:
                queue.append(i)
                visit[i] = True
                depths[i] = depths[point] + 1
        if len(queue) == 0:
            for i in range(n):
                if visit[i] is False:
                    queue.append(i)
                    depths[i] = -1
                    visit[i] = True

    for i in range(n):
        print('%d %d' % (i + 1, depths[i]))
