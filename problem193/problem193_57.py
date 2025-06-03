from itertools import product
H, W, K = map(int, input().split())
G = [list(map(int, list(input()))) for _ in range(H)]

ans = float("inf")

for pattern in product([0, 1], repeat = H - 1):
    div = [0] + [i for i, p in enumerate(pattern, 1) if p == 1] + [H]
    rows = []
    for i in range(len(div) - 1):
        row = []
        for j in range(W):
            tmp = 0
            for k in range(div[i], div[i + 1]):
                tmp += G[k][j]
            row.append(tmp)
        rows.append(row)
        
    flag = True
    for row in rows:
        if [r for r in row if r > K]:
            flag = False
            break
    if not flag:
        continue

    tmp_ans = 0
    cnt = [0] * len(rows)
    w = 0

    while w < W:
        for r in range(len(rows)):
            cnt[r] += rows[r][w]
        if [c for c in cnt if c > K]:
            cnt = [0] * len(rows)
            tmp_ans += 1
            w -= 1
        w += 1
    
    tmp_ans += pattern.count(1)
    ans = min(ans, tmp_ans)

print(ans)