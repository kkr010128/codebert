MOD = 10 **9 + 7
INF = 10 ** 10

def main():
    n,m,l = map(int,input().split())
    dist = [[INF] * n for _ in range(n)]  
    for _ in range(m):
        a,b,c = map(int,input().split())
        a -= 1
        b -= 1
        dist[a][b] = c
        dist[b][a] = c

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])

    cnt = [[INF] * n for _ in range(n)]   
    for i in range(n):
        for j in range(n):
            if dist[i][j] <= l:
                cnt[i][j] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                cnt[i][j] = min(cnt[i][j],cnt[i][k] + cnt[k][j])
    
    q = int(input())
    for _ in range(q):
        s,t = map(int,input().split())
        s -= 1
        t -= 1
        print(cnt[s][t] - 1 if cnt[s][t] != INF  else -1)       
if __name__ == '__main__':
    main()