# sr,sc,gr,gcの総当りでTLEした
# goalは各startに対して最も遠い地点とすればよい

def main():
    from collections import deque

    dd = 0, 1, 0, -1

    H, W = map(int, input().split())
    G = [input() for _ in range(H)]

    def dist(sr, sc):
        if G[sr][sc] == '#':
            return -1

        memo = [[-1] * W for _ in range(H)]

        dq = deque()
        dq.append((sr, sc, 0))
        memo[sr][sc] = 0
        while dq:
            r, c, d = dq.popleft()
            nd = d + 1
            for i in range(4):
                nr = r + dd[i]
                nc = c + dd[i ^ 1]
                if not (0 <= nr < H and 0 <= nc < W):
                    continue
                if ~memo[nr][nc]:
                    continue
                if G[nr][nc] == '#':
                    continue
                dq.append((nr, nc, nd))
                memo[nr][nc] = nd

        return d

    ans = 0
    for sr in range(H):
        for sc in range(W):
            ans = max(ans, dist(sr, sc))

    print(ans)


if __name__ == '__main__':
    main()
