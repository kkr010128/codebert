# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# from decorator import stop_watch
# 
# 
# @stop_watch
def solve(H, W, Ss):
    Ss = ['#' + S + '#' for S in Ss]
    Ss = ['#' * (W + 2)] + Ss + ['#' * (W + 2)]
    # for S in Ss:
    #     print(S)
    ans = 0
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if Ss[i][j] == '#':
                continue
            visited = [[-1] * (W + 2) for _ in range(H + 2)]
            now = 0
            visited[i][j] = now
            q = deque([(i, j, now)])
            while q:
                x, y, n = q.popleft()
                # for v in visited:
                #     print(v)
                # input()
                if Ss[x + 1][y] == '.' \
                        and visited[x + 1][y] < 0:
                    q.append((x + 1, y, n + 1))
                    visited[x + 1][y] = n + 1
                if Ss[x - 1][y] == '.' \
                        and visited[x - 1][y] < 0:
                    q.append((x - 1, y, n + 1))
                    visited[x - 1][y] = n + 1
                if Ss[x][y + 1] == '.' \
                        and visited[x][y + 1] < 0:
                    q.append((x, y + 1, n + 1))
                    visited[x][y + 1] = n + 1
                if Ss[x][y - 1] == '.' \
                        and visited[x][y - 1] < 0:
                    q.append((x, y - 1, n + 1))
                    visited[x][y - 1] = n + 1
            ans = max(ans, max([max(v) for v in visited]))
    print(ans)


if __name__ == '__main__':
    H, W = map(int, input().split())
    Ss = [input() for _ in range(H)]
    solve(H, W, Ss)
