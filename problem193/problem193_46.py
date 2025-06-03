h, w, k = map(int, input().split())
s = [input() for _ in range(h)]

INF = 10 ** 20
ans = INF
for div in range(1 << (h - 1)):
    id = []
    g = 0
    for i in range(h):
        id.append(g)
        if div >> i & 1:
            g += 1
    g += 1

    c = [[0 for _ in range(w)] for _ in range(g)]
    for i in range(h):
    	for j in range(w):
            c[id[i]][j] += (s[i][j] == "1")

    tmp_ans = g - 1
    now = [0] * g

    def add(j):
        for i in range(g):
            now[i] += c[i][j]
            if now[i] > k:
                return False
        return True

    for j in range(w):
        if not add(j):
            tmp_ans += 1
            now = [0] * g
            if not add(j):
                tmp_ans = INF
                break

    # impossible = 0
    # for j in range(w):
    #     if impossible:
    #         tmp_ans = INF
    #         break
    #     for i in range(g):
    #         if c[i][j] > k:
    #             impossible = 1
    #             break
    #         now[i] += c[i][j]
    #         if now[i] > k:
    #             now = [c[gi][j] for gi in range(g)]
    #             tmp_ans += 1
    #             continue

    ans = min(ans, tmp_ans)

print(ans)