import sys
input = sys.stdin.buffer.readline
from collections import deque

def main():
    N,u,v = map(int,input().split())
    con = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        con[a-1].append(b-1)
        con[b-1].append(a-1)

    aq = deque([v-1])
    adist = [0 for _ in range(N)]
    edge = []
    go = [True for _ in range(N)]
    go[v-1] = False
    while aq:
        now = aq.pop()
        for fol in con[now]:
            if go[fol]:
                adist[fol] = adist[now] + 1
                go[fol] = False
                if con[fol] == [now]:
                    edge.append(fol)
                else:
                    aq.append(fol)
    
    tq = deque([u-1])
    tdist = [0 for _ in range(N)]
    _go = [True for _ in range(N)]
    _go[u-1] = False
    while tq:
        now = tq.pop()
        for fol in con[now]:
            if _go[fol]:
                tdist[fol] = tdist[now] + 1
                _go[fol] = False
                tq.append(fol)

    ans = 0
    for num in edge:
        a,t = adist[num],tdist[num]
        if a <= t:
            continue
        else:
            ans = max(ans,a-1)
                
    print(ans)

if __name__ == "__main__":
    main()
