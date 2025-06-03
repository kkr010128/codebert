from sys import stdin

global time
time = 0

def dfs(graph,start,state,discover,finish):

    state[start-1] = 1
    global time
    time = time + 1
    discover[start-1] = time
    # print str(time) + " go to " + str(start)

    neighbours = sorted(graph[start])

    for neighbour in neighbours:
        if state[neighbour-1] == 0:
            dfs(graph,neighbour,state,discover,finish)

    state[start-1] = 2
    time = time + 1
    finish[start - 1] = time
    # print str(time) + " out of " + str(start)

def main():
    # g = {1: [2, 3],
    #      2: [3, 4],
    #      3: [5],
    #                     4: [6],
    #                     5: [6],
    #                     6: []}



    # deal with input
    n = int(stdin.readline())

    g = {}

    d = [0]*n
    f = [0]*n

    all_vertex = []

    for i in xrange(n):
        entry = [int(s) for s in stdin.readline().split()[2:]]
        g[i+1] = entry
        all_vertex.append(i+1)



    # exp = []
    # state represent vertex visited state: 0 not visited 1 visiting 2 finished
    state = [0]*n

    for node in all_vertex:
        if state[node-1] == 0:
            dfs(g,node,state,d,f)

    # print  'state ' + str(state)

    # print 'd' + str(d)
    # print 'f' + str(f)

    # deal with output
    for i in xrange(n):
        print str(i+1) + ' ' + str(d[i]) + ' ' + str(f[i])

main()
