from collections import deque

def main():

    inf = 1000000007
    n = int(input())
    e = [[] for _ in range(n)]
    d = [inf]*n

    for i in range(n):
        m = list(map(int,input().split()))
        for j in range(2,len(m)):
            e[m[0]-1].append(m[j]-1)

    d[0] = 0
    dq = deque([])
    dq.append([0,0])
    while dq:
        c,v = dq.popleft()
        for u in e[v]:
            if d[u]==inf:
                d[u] = c+1
                dq.append([c+1,u])

    for i in range(n):
        if d[i]==inf:print (i+1,-1)
        else        :print (i+1,d[i])

if __name__ == '__main__':
    main()


