def main():
    import sys
    from copy import deepcopy
    input = sys.stdin.readline
    R, C, K = [int(x) for x in input().strip().split()]
    G = [[0] * (C+1) for r in range(R+1)]
    for k in range(K):
        r, c, v = [int(x) for x in input().strip().split()]
        G[r][c] = v
    # for r in range(R+1):
    #     print(G[r])
    ans = [[[0] * 4 for _ in range(C+1)] for _ in range(2)]
    for r in range(1, R+1):
        for c in range(1, C+1):
            ans[r%2][c][0] = max(ans[(r-1)%2][c][-1], ans[r%2][c-1][0])
            for i in range(1, 4):
                ans[r%2][c][i] = max(ans[(r-1)%2][c][3], ans[r%2][c-1][i], ans[(r-1)%2][c][3]+G[r][c], ans[r%2][c-1][i-1]+G[r][c])

    print(max(ans[R%2][-1]))

if __name__ == '__main__':
    main()
