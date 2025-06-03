def main():
    H, W, M = [int(s) for s in input().split()]
    cols = [0] * W
    rows = [0] * H
    bombs = set()
    for _ in range(M):
        x, y = [int(s)-1 for s in input().split()]
        bombs.add((x, y))
        cols[y] += 1
        rows[x] += 1

    sc = sorted([(c, i) for i, c in enumerate(cols)], reverse=True)
    sr = sorted([(c, i) for i, c in enumerate(rows)], reverse=True)
    best = 0
    for v1, c in sc:
        for v2, r in sr:
            if v1 + v2 <= best:
                break
            score = v1 + v2
            if (r, c) in bombs:
                score -= 1
            best = max(best, score)
    print(best)

main()