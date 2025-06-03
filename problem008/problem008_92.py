def main():
    n = input()
    A = []
    s = []
    B = [[0,0] for i in xrange(n)]
    for i in xrange(n):
        A.append(map(int,raw_input().split()))

    color = [-1]*n
    d = [0]*n
    f = [0]*n
    t = 0
    
    for i in xrange(n):
        if color[i] == -1:
            t = dfs(i,t,color,d,f,A,n)

    for i in xrange(n):
        print i+1, d[i], f[i]


def dfs(u,t,color,d,f,A,n):
    t += 1
    color[u] = 0
    d[u] = t
    for i in A[u][2:]:
        if (color[i-1] == -1):
            t = dfs(i-1,t,color,d,f,A,n)
    color[u] = 1
    t += 1
    f[u] = t
    return t

if __name__ == '__main__':
    main()