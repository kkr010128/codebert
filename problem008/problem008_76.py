def DFS(G):
    ans = [0] + [[0,0,0] for _ in range(len(G))]
    def main(G,i):
        ans[0] += 1
        ans[i] = [i, ans[0], ans[0]]
        for j in sorted(G[i-1][2:]):
            if ans[j][0] == 0: main(G,j)
        ans[0] += 1
        ans[i][2] = ans[0]
    for u in G:
        if ans[u[0]][0] == 0: main(G,u[0])
    return ans[1:]


if __name__=='__main__':
    n = int(input())
    G = [list(map(int,input().split())) for _ in range(n)]
    for out in DFS(G): print(*out)