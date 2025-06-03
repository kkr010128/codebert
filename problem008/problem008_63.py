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

    visit[0] = True
    frist[0] = s = 1
    stack = [0]

    while len(stack) != 0:
        point = stack.pop(-1)
        flag = False
        for i in range(n):
            if graph[point][i] == 1 and visit[i] is False:
                visit[i] = True
                flag = True
                s += 1
                frist[i] = s
                stack.append(point)
                stack.append(i)
                break
        if flag is False:
            s += 1
            end[point] = s
        
        if len(stack) == 0:
            for i in range(n):
                if visit[i] is False:
                    visit[i] = True
                    s += 1
                    frist[i] = s
                    stack.append(i)
                    break
            
    for i in range(n):
        print('%d %d %d' % (i+1, frist[i], end[i]))
