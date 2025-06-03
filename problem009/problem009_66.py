import sys

global status, d
status = {}
d=0

def bfs(keys, GRAPH, depth=0):
    global status
    if depth>10: quit

    buf =[]
    for e in keys:
        if status[e]==-1:
            status[e]=depth
            for e2 in GRAPH[e]:
                try:
                    if status[e2] == -1:
                        buf.append(e2)
                except:
                    pass
    if buf !=[]:
        bfs(buf, GRAPH, depth+1)
    return

n = int(raw_input())
x = {}
for i in range(n):
    seq = map(int,raw_input().split())
    key = seq[0]
    if key != 0:
        x[key] = seq[2:]
    else:
        x[key]=[]
    status[key] = -1

for e in x.keys():
    if e == 1:
        bfs([e], x)

for e in x.keys():
    print e, status[e]