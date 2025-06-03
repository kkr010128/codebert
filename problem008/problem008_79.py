n = int(input())

graph = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    if tmp[1] == 0:
        graph.append([])
    else:
        graph.append(tmp[2:])
#print(graph)

seen = [0]*n
to_do = []
in_list = [0]*n
out_list = [0]*n
count = 0

def dfs(v):
    #print(v)
    global count
    if seen[v] == 0:
        seen[v] = 1
        count += 1
        in_list[v] = count
        to_do = graph[v]
        #print(in_list)
        #print(to_do)
        if len(to_do) > 0:
            for i in to_do:
                dfs(i-1)
        count += 1
        out_list[v] = count
        #print(out_list)
while True:
    if 0 in seen:
        k = seen.index(0)
        dfs(k)
    else:
        break

for i in range(n):
    print("{} {} {}".format(i+1,in_list[i],out_list[i]))
