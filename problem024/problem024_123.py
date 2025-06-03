N, K = [int(s) for s in raw_input().split()]
ws = [int(raw_input()) for _ in xrange(N)]
lo, hi = max(ws) - 1, sum(ws)

while hi - lo > 1:
    p = P = (lo + hi) / 2
    k = 1
    for w in ws:
        if w > p:
            p = P
            k += 1
        p -= w
    if k <= K:
        hi = P
    else:
        lo = P

print hi