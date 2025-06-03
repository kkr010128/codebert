from collections import Counter


def solve():
    H, W, M = map(int, input().split())
    dh, dw = Counter(), Counter()
    used = set()

    for _ in range(M):
        h, w = map(int, input().split())
        dh[h] += 1
        dw[w] += 1
        used.add((h, w))

    ih = dh.most_common()
    iw = dw.most_common()

    h, counth = ih[0]
    w, countw = iw[0]

    s = counth + countw
    ans = counth + countw - ((h, w) in used)

    for h, counth in ih:
        for w, countw in iw:
            if counth+countw < s or ans == s:
                break
            b = counth + countw - ((h, w) in used)
            ans = max(ans, b)
    print(ans)


solve()