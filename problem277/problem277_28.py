H, W, K = map(int, input().split())
a = [input() for _ in range(H)]
ans = [[-1 for _ in range(W)] for _ in range(H)]
i_cut_time = 0
j_cut_time = 0
for i in range(H):
    if '#' in a[i]:
        i_cut_time += 1
i_cut = []
start = 0
goal = -1
for i in range(H):
    if len(i_cut) == i_cut_time-1:
        break
    if '#' in a[i]:
        goal = i
        i_cut.append([start, goal, i])
        start = goal+1
for i in range(start, H):
    if '#' in a[i]:
        i_cut.append([start, H-1, i])
# print(i_cut)
cnt = 1
for s, g, p in i_cut:
    j_cut = []
    jstart = 0
    jgoal = -1
    for i in range(W):
        if len(j_cut) == a[p].count('#')-1:
            break
        if a[p][i] == '#':
            jgoal = i
            j_cut.append([jstart, jgoal])
            jstart = jgoal+1
    j_cut.append([jstart, W-1])
    # print(s, g, p, j_cut)
    # for i in range(s, g+1):
    for js, jg in j_cut:
        for j in range(js, jg+1):
            for i in range(s, g+1):
                # print(i, j, cnt)
                ans[i][j] = cnt
        cnt += 1

# print(*ans, sep='\n')
for i in range(H):
    print(*ans[i])