def main():
    H, W, M = map(int, input().split())
    # H, W, M = (3 * 10 ** 5, 3 * 10 ** 5, 3 * 10 ** 5)

    row = [0] * (H + 1)
    row_set = [set() for _ in range(H+1)]
    column = [0] * (W + 1)
    column_set = [set() for _ in range(W+1)]
    # import random
    ms = []
    positions = set()
    for m in range(M):
        h, w = map(int, input().split())

        positions.add((h, w))
        # h, w = (random.randrange(3*10**5), random.randrange(3*10**5))
        row[h] += 1
        row_set[h].add(w)

        column[w] += 1
        column_set[w].add(h)



    max_rows = set()
    maxR = -1
    for i, v in enumerate(row[1:]):
        if v > maxR:
            max_rows = set()
            max_rows.add(i+1)
            maxR = v
        elif v == maxR:
            max_rows.add(i+1)


    max_cols = set()
    maxC = -1
    for i, v in enumerate(column[1:]):
        if v > maxC:
            max_cols = set()
            max_cols.add(i+1)
            maxC = v
        elif v == maxC:
            max_cols.add(i + 1)


    for y in max_rows:
        for x in max_cols:
            if not (y, x) in positions:
                print(maxR + maxC)
                exit()
    print(maxR + maxC - 1)
main()
