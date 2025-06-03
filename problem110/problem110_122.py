def solve():
    H,W,K = [int(i) for i in input().split()]
    grids = []
    for i in range(H):
        row = input()
        grids.append(row)

    import itertools
    rows = list(range(H))
    row_combis = set([])
    for i in range(H+1):
        tmp = itertools.combinations(rows, i)
        row_combis |= set(tmp)
    columns = list(range(W))
    column_combis = set([])
    for i in range(W+1):
        tmp = itertools.combinations(columns, i)
        column_combis |= set(tmp)

    ans = 0
    for row_combi in row_combis:
        for column_combi in column_combis:
            num_black = 0
            for i in range(H):
                for j in range(W):
                    if i in row_combi:
                        continue
                    if j in column_combi:
                        continue
                    if grids[i][j] == '#':
                        num_black += 1
            if num_black == K:
                ans += 1
    print(ans)


if __name__ == "__main__":
    solve()