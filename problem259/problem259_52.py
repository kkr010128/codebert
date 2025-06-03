import sys,heapq
input = sys.stdin.readline
def main():
    n,u,v = map(int,input().split())
    u,v = u-1,v-1

    edge = [[] for _ in range(n)]

    for _ in [0]*(n-1):
        a,b = map(int,input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)

    #cost:vからの距離
    cost = [0]*n
    new = [v]
    c = 1
    while len(new):
        tank = []
        for e in new:
            for go in edge[e]:
                if go != v and cost[go] == 0:
                    cost[go] = c
                    tank.append(go)
        c += 1
        new = tank

    if cost[u]%2 == 1:
        res = cost[u]//2
        now = u
        for _ in [0]*res:
            for e in edge[now]:
                if cost[now] > cost[e]:
                    now = e
        
        new = [now]
        while len(new):
            tank = []
            for e in new:
                for go in edge[e]:
                    if cost[go] > cost[e]:
                        tank.append(go)
            res += 1
            new = tank
        
        print(res-1)

    else:
        res = cost[u]//2-1
        now = u
        for _ in [0]*res:
            for e in edge[now]:
                if cost[now] > cost[e]:
                    now = e
        
        new = [now]
        while len(new):
            tank = []
            for e in new:
                for go in edge[e]:
                    if cost[go] > cost[e]:
                        tank.append(go)
            res += 1
            new = tank
        
        print(res)



if __name__ == '__main__':
    main()