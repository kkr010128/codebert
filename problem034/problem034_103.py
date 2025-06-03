d, q = list(map(int, input().split())), int(input())
dd = {v: k for k, v in enumerate(d)}
dms = ((1, 2, 4, 3), (0, 3, 5, 2), (0, 1, 5, 4), (0, 4, 5, 1), (0, 2, 5, 3), (1, 3, 4, 2))

while q:
    t, f = map(int, input().split())
    dm = dms[dd[t]]
    print(d[dm[(dm.index(dd[f]) + 1) % 4]])
    q -= 1