from itertools import product

h, w, k = list(map(int, input().split()))
s = [list(map(int, list(input()))) for i in range(h)]
INF = float("inf")
ans = INF
for bits in product([0, 1], repeat=h-1):
    cnt = sum(bits)
    cuts = [0]+[i + 1 for i, x in enumerate(bits) if x == 1]+[h]
    data = [[0]*w for _ in range(len(cuts)-1)]
    for i in range(len(cuts)-1):
        target = s[cuts[i]:cuts[i+1]]
        for tt in target:
            for j, t in enumerate(tt):
                data[i][j] += t
    check = [[0]*(w+1) for _ in range(len(data))]
    flag = False
    for j in range(w):
        if flag:
            continue
        change = False
        for i in range(len(data)):
            if check[i][j] + data[i][j] > k:
                change = True
                break
        if change:
            for i in range(len(data)):
                if data[i][j] <= k:
                    check[i][j+1] = data[i][j]
                else:
                    flag = True
                    break
            cnt += 1
        else:
            for i in range(len(data)):
                check[i][j+1] = check[i][j] + data[i][j]
    if flag:
        continue
    ans = min(ans, cnt)
print(ans)
