h, w, k = [int(i) for i in input().split()]
s = [input() for _ in range(h)]

ans = float("inf")
for i in range(2 ** (h - 1)):
    a = 0
    for j in range(h - 1):
        if (i >> j) & 1 == 1:
            a += 1
    c = a
    b = [0] * (c + 1)
    ok2 = True
    for j in range(w):
        tmp = 0
        for l in range(h):
            if s[l][j] == "1":
                b[tmp] += 1
            if (i >> l) & 1 == 1:
                tmp += 1

        ok = True
        for l in b:
            if l > k:
                ok = False

        if not ok:
            a += 1
            b = [0] * (c + 1)

            tmp = 0
            for l in range(h):
                if s[l][j] == "1":
                    b[tmp] += 1
                if (i >> l) & 1 == 1:
                    tmp += 1

            ok = True
            for l in b:
                if l > k:
                    ok = False
            if not ok:
                ok2 = False
                break
    if ok2:
        ans = min(ans, a)

print(ans)
