# 隣接リスト
n = int(input())

graph = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    if tmp[1] == 0:
        graph.append([])
    else:
        graph.append(tmp[2:])

#print(graph)
check = [0]*n
count = 0
go = [0]*n
back = [0]*n

def dfs(v):
    #print(v)
    global count
    if check[v] == 0:
        check[v] = 1
        count += 1
        go[v] = count
        tolist = graph[v]
        if len(tolist) > 0:
            for i in tolist:
                dfs(i-1)
        count += 1
        back[v] = count

while True:
    if 0 in check:
        k = check.index(0)
        dfs(k)
    else:
        break

#print("check\t:{}".format(check))
#print("go\t:{}".format(go))
#print("back\t:{}".format(back))

for i in range(n):
    print("{} {} {}".format(i+1, go[i], back[i]))

