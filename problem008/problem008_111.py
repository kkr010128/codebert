from collections import deque

#スタックを使った深さ優先探索の実装
l = int(input())
rlist = []
for i in range(l):
    li = list(map(int, input().split()))
    rlist.append(deque([ll-1 for ll in li[2:]]))


color = ['white'] * l
find_time = [0] * l
stop_time = [0] * l
stack = []
time = 0

def dfs(u):
    global time

    stack.append(u)
    color[u] = 'gray'
    time += 1
    find_time[u] = time

    while len(stack) > 0:
        #print(stack)
        #print(color)
        #print(rlist)

        u = stack[-1]
        #頂点uにまだ訪問すべき頂点が残っているなら
        if len(rlist[u]) > 0:
            if color[rlist[u][0]] == 'white':
                time += 1
                find_time[rlist[u][0]] = time
                color[rlist[u][0]] = 'gray'
                stack.append(rlist[u][0])
            rlist[u].popleft()
        #頂点uにもう訪問すべき頂点が残っていないなら
        else:
            time += 1
            stop_time[u] = time
            color[u] = 'black'
            stack.pop()

for i in range(l):
    if color[i] == 'white':
        dfs(i)
for i in range(len(find_time)):
    print(str(i+1) + ' ' + str(find_time[i]) + ' ' + str(stop_time[i]))
