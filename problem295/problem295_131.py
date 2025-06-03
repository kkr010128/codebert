import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10, 6))

def main():
    n, m, l = map(int, input().split())
    d = [[float("inf") for _ in range(n)] for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        d[a-1][b-1] = c
        d[b-1][a-1] = c
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
    
    dl = [[float("inf") for _ in range(n)] for _ in range(n)]
    for i in range(n):
        d[i][i] = 0

    for i in range(n):
        for j in range(i+1, n):
            if i != j and d[i][j] <= l:
                dl[i][j] = 1
                dl[j][i] = 1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dl[i][j] > dl[i][k] + dl[k][j]:
                    dl[i][j] = dl[i][k] + dl[k][j]
    
    q = int(input())
    for _ in range(q):
        s, t = map(int, input().split())
        if dl[s-1][t-1] == float("inf"):
            print(-1)
        else:
            print(dl[s-1][t-1] - 1)


if __name__ == '__main__':
    main()
