def main():
    n = input()
    A = []
    for i in xrange(n):
        A.append(map(int,raw_input().split()))

    c,d = bfs(n,A)

    for i in xrange(n):
        if c[i] == -1:
            print i+1, -1
        else:
            print i+1, d[i]

def bfs(n,A):
    color = [-1]*n
    d = [-1]*n
    Q = []
    d[0] = 0
    Q.append(0)
    while(True):
        if len(Q)==0:
            break
        u = Q.pop(0)
        for i in A[u][2:]:
            if color[i-1] == -1:
                color[i-1] = 0
                d[i-1] = d[u]+1
                Q.append(i-1)
        color[u] = 1
    return color, d    

if __name__ == '__main__':
    main()