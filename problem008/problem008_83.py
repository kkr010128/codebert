n = int(raw_input())

d = [0] * n
f = [0] * n
M = [[0]*n for _ in xrange(n)]
color = [0] * n
tt = 0
WHITE = 0
GRAY = 1
BLACK = 2

def dfs_visit(u):
    global tt
    color[u] = GRAY
    tt += 1
    d[u] = tt
    for v in xrange(n):
        if M[u][v] == 0:
            continue
        if color[v] == WHITE:
            dfs_visit(v)
    color[u] = BLACK
    tt += 1
    f[u] = tt
    return 0

def dfs():
    for u in xrange(n):
        if color[u] == WHITE:
            dfs_visit(u)
    for u in xrange(n):
        print "{} {} {}".format(u+1, d[u], f[u])
    return 0

def main():
    for i in xrange(n):
        a = map(int, raw_input().split())
        u = a[0]-1
        k = a[1]
        for j in xrange(k):
            v = a[j+2] -  1
            M[u][v] = 1
    
    dfs()
    return 0

main()