H, W, K = map(int, input().split(' '))
ls, rst = [], 0
for i in range(H):
    ls.append(input())
for i in range(1 << H):
    for j in range(1 << W):
        cnt = 0
        for s in range(H):
            if i >> s & 1:
                continue
            for t in range(W):
                if j >> t & 1:
                    continue
                if ls[s][t] == '#':
                    cnt += 1
        if cnt == K:
            rst += 1
print(rst)